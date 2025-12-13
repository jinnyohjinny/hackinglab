# Network Health Check

A professional web application for network diagnostics and connectivity testing.

## Features

- Real-time network connectivity testing
- ICMP ping diagnostics with detailed output
- Network latency monitoring and history
- Professional terminal-style output display
- Rate limiting to prevent abuse (10 requests per minute)
- Clean, intuitive user interface
- Responsive design for desktop and mobile

## Quick Start

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Navigate to this directory:
```bash
cd level-13
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

### GET /diagnostics/ping

Test network connectivity to a target host.

**Parameters:**
- `target` (required): The IP address or hostname to ping
  - Example: `8.8.8.8`, `google.com`, `localhost`

**Example Request:**
```bash
curl "http://localhost:8080/diagnostics/ping?target=8.8.8.8"
```

**Example Response:**
```json
{
  "status": "completed",
  "target": "8.8.8.8",
  "output": "PING 8.8.8.8 (8.8.8.8): 56 data bytes\n64 bytes from 8.8.8.8: seq=0 ttl=117 time=12.4 ms\n64 bytes from 8.8.8.8: seq=1 ttl=117 time=11.8 ms\n\n--- 8.8.8.8 ping statistics ---\n2 packets transmitted, 2 packets received, 0% packet loss\nround-trip min/avg/max = 11.8/12.1/12.4 ms"
}
```

**Error Response (Rate Limit):**
```json
{
  "error": "Rate limit exceeded. Please try again later."
}
```

**Error Response (Missing Parameter):**
```json
{
  "error": "Target parameter is required"
}
```

### GET /

Main dashboard with ping diagnostic tool interface.

### GET /about

Information about the Network Health Check application.

### GET /contact

Contact information and support details.

## Architecture

- **Backend**: Flask (Python 3.11)
- **Frontend**: HTML5, Bootstrap 5, Vanilla JavaScript
- **Container**: Alpine Linux with Python 3.11
- **Web Server**: Flask development server

## Application Structure

```
level-13/
├── app.py                  # Main Flask application
├── templates/
│   ├── index.html         # Main dashboard
│   ├── about.html         # About page
│   └── contact.html       # Contact page
├── static/
│   └── css/
│       └── style.css      # Custom styles
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Use Cases

- Troubleshooting network connectivity issues
- Monitoring server availability
- Testing DNS resolution
- Verifying network configuration changes
- Quick network diagnostics for system administrators

## Security Features

- Rate limiting (10 requests per minute per IP)
- Input validation
- Secure headers
- Production-ready configuration

## Maintenance Schedule

Scheduled maintenance every Sunday 2-4 AM UTC.

## License

For educational and security research purposes only.
