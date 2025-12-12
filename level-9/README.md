# URL Sanitizer & Path Validator

A professional enterprise-grade URL security analysis and path validation tool built with Flask.

## Features

- **URL Security Analyzer**: Validate URLs against multiple security checks
- **Path Parser**: Parse and analyze URL paths for compliance
- **Real-time Analysis**: Instant security validation with advanced pattern matching
- **Security Logs**: Monitor system activity and security events
- **System Statistics**: Track performance metrics and request analytics

## Requirements

- Docker
- Docker Compose

## Installation & Setup

1. Clone or navigate to this directory:
```bash
cd level-9
```

2. Build and start the application:
```bash
docker compose up -d
```

3. Access the application:
```
http://localhost:5000
```

## Usage

### URL Validation
1. Navigate to the "URL Security Analyzer" section
2. Enter a URL to validate
3. Click "Analyze URL" to see security checks

### Path Parsing
1. Navigate to the "Path Parser" section
2. Enter a path to parse
3. Click "Parse Path" to see the results

### View Logs
- Click "Refresh Logs" in the Security Logs section to view recent activity

### System Statistics
- Click "Load Statistics" to view system performance metrics

## Stopping the Application

```bash
docker compose down
```

## Technology Stack

- **Backend**: Flask (Python 3.9)
- **Frontend**: Bootstrap 5, Vanilla JavaScript
- **Container**: Docker with Alpine Linux

## Security Features

- Production-grade error handling
- Input validation and sanitization
- Real-time security analysis
- Comprehensive logging system

---

**SecureTools Pro** - Enterprise URL Security Solutions
