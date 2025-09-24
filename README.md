# home-health-site - Docker Setup

A simple Docker setup for the home-health-site adult care website using nginx:alpine.

## Quick Start

### Build the Docker image:
```bash
docker build -t home-health-site .
```

### Run the container:
```bash
docker run -d -p 8080:80 --name home-health-site home-health-site
```

The website will be available at: http://localhost:8080

### For Cloudflare Tunnel:
Use any available port (e.g., 8080, 8081, 3000) when running the container, then point your Cloudflare tunnel to that port.

## Docker Compose Deployment

For easy deployment on a VPS or server, use Docker Compose:

### Deploy with Docker Compose:
```bash
docker-compose up -d
```

### Update to latest image:
```bash
docker-compose pull && docker-compose up -d
```

### View logs:
```bash
docker-compose logs -f home-health-site
```

### Stop the service:
```bash
docker-compose down
```

## Docker Commands

### Stop the container:
```bash
docker stop home-health-site
```

### Remove the container:
```bash
docker rm home-health-site
```

### View running containers:
```bash
docker ps
```

### View container logs:
```bash
docker logs home-health-site
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
