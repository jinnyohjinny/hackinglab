# System Health Monitor

A professional web application for monitoring system health and performance metrics.

## Features

- Real-time system metrics monitoring
- Memory usage tracking
- CPU load monitoring
- Disk space analysis
- Network status monitoring
- Clean, modern dashboard interface
- RESTful API endpoints

## Quick Start

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone or navigate to this directory:
```bash
cd level-12
```

2. Build and start the application:
```bash
docker-compose up -d
```

3. Access the application:
```
http://localhost:8080
```

### Stopping the Application

```bash
docker-compose down
```

## API Endpoints

### GET /cgi-bin/system-info.cgi

Retrieve system component information.

**Parameters:**
- `component` (required): The system component to check
  - Valid values: `memory`, `cpu`, `disk`, `network`

**Example Request:**
```bash
curl "http://localhost:8080/cgi-bin/system-info.cgi?component=memory"
```

**Example Response:**
```json
{
  "status": "ok",
  "component": "memory",
  "data": "Memory: 2.4GB / 8GB (30%)"
}
```

## Architecture

- **Backend**: Perl 5 with CGI.pm
- **Web Server**: Apache 2 with CGI support
- **Frontend**: HTML5, Bootstrap 5, Vanilla JavaScript
- **Container**: Alpine Linux 3.18

## Development

The application structure:
```
level-12/
├── cgi-bin/
│   ├── index.cgi          # Main dashboard
│   └── system-info.cgi    # API endpoint
├── static/
│   ├── css/
│   │   └── styles.css     # Custom styles
│   └── js/
│       └── app.js         # Frontend logic
├── Dockerfile
├── docker-compose.yml
├── httpd.conf
└── README.md
```

## License

For educational and security research purposes only.
