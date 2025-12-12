# URL Path Analyzer - Enterprise Security Suite

A professional URL path security analysis tool for enterprise environments.

## Features

- **Real-time Path Analysis**: Analyze URL paths for security threats and malformed inputs
- **Advanced Threat Detection**: Identify suspicious patterns and potential attack vectors
- **Security Scoring**: Comprehensive risk assessment for each analyzed path
- **Enterprise Logging**: Detailed activity logs and monitoring
- **High Performance**: Process thousands of requests per second

## Quick Start

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone or navigate to this directory:
```bash
cd level-10
```

2. Build and start the application:
```bash
docker compose up -d
```

3. Access the application at `http://localhost:5000`

### Stopping the Application

```bash
docker compose down
```

## Usage

### Web Interface

Visit `http://localhost:5000` to access the URL Path Analyzer dashboard.

Features available:
- Path scanning and validation
- Real-time analytics
- Activity logging
- Security scoring

### API Endpoints

- `GET /` - Main dashboard
- `GET /about` - About page
- `GET /contact` - Contact information
- `GET /api/health` - Health check endpoint
- `GET /api/analytics` - System analytics
- `POST /api/scan` - Scan a URL path

### Path Analysis

The application analyzes URL paths accessed directly via the URL:

```
http://localhost:5000/username
```

This will display a personalized greeting based on the path.

## Architecture

- **Backend**: Flask (Python 3.9)
- **Frontend**: Tailwind CSS, Vanilla JavaScript
- **Container**: Docker with Alpine Linux
- **Web Server**: Flask development server (production mode)

## Version

Current Version: 2.1.4

## License

For educational and security training purposes only.

---

© 2025 PathAnalyzer Enterprise Security Suite
