# Text Transformer

A professional web-based text transformation utility that allows users to apply pattern-based replacements to text content. Built with PHP and designed for ease of use.

## Features

- **Pattern Matching**: Support for both simple text and regular expression patterns
- **Real-time Transformation**: Instant text processing and results display
- **Clean Interface**: Modern, responsive design with intuitive controls
- **Flexible Input**: Accepts patterns and replacement values for versatile text manipulation

## Technology Stack

- **Backend**: PHP 5.4 with FPM
- **Web Server**: Nginx
- **Container**: Docker with Alpine Linux base
- **Frontend**: HTML5, CSS3

## Quick Start

### Prerequisites

- Docker
- Docker Compose

### Installation & Running

1. Navigate to the project directory:
```bash
cd level-6
```

2. Build and start the application:
```bash
docker compose up -d
```

3. Access the application in your browser:
```
http://localhost:8006
```

### Stopping the Application

```bash
docker compose down
```

## Usage Examples

### Example 1: Simple Text Replacement
- **Message**: `Hello World`
- **Pattern**: `World`
- **Replacement**: `Universe`
- **Result**: `Hello Universe`

### Example 2: Regex Pattern Matching
- **Message**: `My phone is 123-456-7890`
- **Pattern**: `/[0-9]+/`
- **Replacement**: `XXX`
- **Result**: `My phone is XXX-XXX-XXXX`

### Example 3: Case-Insensitive Replacement
- **Message**: `Welcome to the WORLD`
- **Pattern**: `/world/i`
- **Replacement**: `Universe`
- **Result**: `Welcome to the Universe`

## Application Structure

```
level-6/
├── docker-compose.yml    # Docker Compose configuration
├── Dockerfile           # Container build instructions
├── nginx.conf          # Nginx web server configuration
├── src/
│   ├── index.php       # Main application file
│   └── assets/
│       └── style.css   # Application styles
└── README.md          # This file
```

## Development

The application uses volume mounting for the `src` directory, allowing for live code updates without rebuilding the container.

To view logs:
```bash
docker compose logs -f
```

To rebuild after configuration changes:
```bash
docker compose up -d --build
```

## Support

For issues or questions, please refer to the project documentation or contact the development team.

---

**Text Transformer v1.0** - Professional Text Processing Tool
