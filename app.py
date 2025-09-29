from flask import Flask, request, render_template, jsonify
import sqlite3
import datetime
import os

app = Flask(__name__)

# Database path for Docker volume mount
DATABASE_PATH = '/app/data/database.db' if os.path.exists('/app/data') else 'database.db'

# Initialize database
def init_database():
    # Ensure data directory exists
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database on startup
init_database()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/contact', methods=['POST'])
def submit_contact():
    try:
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        
        # Basic validation
        if not name or not email or not message:
            return jsonify({'success': False, 'message': 'All fields are required'}), 400
        
        # Save to database
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO contacts (name, email, message) 
            VALUES (?, ?, ?)
        ''', (name, email, message))
        conn.commit()
        conn.close()
        
        return jsonify({'success': True, 'message': 'Thank you for your message! We will get back to you soon.'})
        
    except Exception as e:
        return jsonify({'success': False, 'message': 'An error occurred. Please try again later.'}), 500

@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, name, email, message, created_at 
            FROM contacts 
            ORDER BY created_at DESC
        ''')
        contacts = cursor.fetchall()
        conn.close()
        
        # Convert to list of dictionaries
        contact_list = []
        for contact in contacts:
            contact_list.append({
                'id': contact[0],
                'name': contact[1],
                'email': contact[2],
                'message': contact[3],
                'created_at': contact[4]
            })
        
        return jsonify({'contacts': contact_list})
        
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve contacts'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
