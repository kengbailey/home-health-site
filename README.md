# Graceful Haven Website - Docker Setup

A simple Docker setup for the Graceful Haven adult care website using nginx:alpine.

## Quick Start

### Build the Docker image:
```bash
docker build -t graceful-haven-website .
```

### Run the container:
```bash
docker run -d -p 8080:80 --name graceful-haven graceful-haven-website
```

The website will be available at: http://localhost:8080

### For Cloudflare Tunnel:
Use any available port (e.g., 8080, 8081, 3000) when running the container, then point your Cloudflare tunnel to that port.

## Docker Commands

### Stop the container:
```bash
docker stop graceful-haven
```

### Remove the container:
```bash
docker rm graceful-haven
```

### View running containers:
```bash
docker ps
```

### View container logs:
```bash
docker logs graceful-haven
```

## Image Details
- Base: nginx:alpine (~20MB compressed)
- Port: 80 (internal)
- Serves static HTML with inline CSS/JS
- No additional configuration required

## Files
- `Dockerfile` - Simple nginx:alpine setup
- `.dockerignore` - Excludes unnecessary files from build context
- `index.html` - Main website file
