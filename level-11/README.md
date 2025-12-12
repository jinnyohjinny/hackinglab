# CloudCode Analyzer

A professional cloud-based code security analysis platform for modern development teams.

## Features

- **Advanced Python Code Analysis**: Static analysis engine to identify security patterns and vulnerabilities
- **Real-time Dashboard**: Monitor your code analysis activity with interactive charts and metrics
- **RESTful API**: Integrate code analysis into your CI/CD pipeline
- **Secure Architecture**: Built with industry-standard security practices
- **Scalable Infrastructure**: Docker-based deployment with Redis and PostgreSQL

## Quick Start

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd level-11
```

2. Start the application:
```bash
docker compose up -d
```

3. Access the application:
```
http://localhost:5000
```

4. Login with demo credentials:
- Username: `demo`
- Password: `demo123`

## Architecture

The application consists of three main services:

- **Web Application**: Flask-based web server with Gunicorn
- **Redis**: Session storage and caching
- **PostgreSQL**: User data and analysis results storage

## Configuration

Environment variables can be configured in `docker-compose.yml`:

- `SECRET_KEY`: Flask secret key for session management
- `REDIS_HOST`: Redis server hostname
- `POSTGRES_HOST`: PostgreSQL server hostname
- `POSTGRES_DB`: Database name
- `POSTGRES_USER`: Database user
- `POSTGRES_PASSWORD`: Database password

## API Documentation

### Analyze Python Code

**Endpoint**: `POST /api/analyze-python`

**Request Body**:
```json
{
  "code_snippet": "your python code here"
}
```

**Response**:
```json
{
  "status": "success",
  "result": "Analysis complete: ...",
  "patterns_detected": ["standard_python_syntax"],
  "risk_level": "low"
}
```

## Development

To run in development mode:

```bash
pip install -r requirements.txt
python app.py
```

## Health Check

The application includes a health check endpoint:

```bash
curl http://localhost:5000/health
```

## Security

- Rate limiting implemented on all API endpoints
- CSRF protection enabled
- Secure headers configured
- Session management with Redis
- Input validation and sanitization

## Support

For support and questions, contact: support@cloudcode.example.com

## License

Copyright © 2024 CloudCode Analyzer. All rights reserved.
