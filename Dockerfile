FROM python:3.11-alpine

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY templates/ templates/

# Create directory for database
RUN mkdir -p /app/data

# Expose port 5000 (Flask default)
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
