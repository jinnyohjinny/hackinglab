# Contacts Manager

A modern, professional contact management system built with PHP. Easily organize and sort your business contacts with an intuitive web interface.

## Features

- **Clean Interface**: Modern, responsive design that works on all devices
- **Sortable Columns**: Click any column header to sort contacts by that field
- **Professional Data**: Pre-loaded with sample business contacts
- **Fast Performance**: Lightweight PHP application with optimized sorting

## Quick Start

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Navigate to the project directory:
```bash
cd level-5
```

2. Start the application:
```bash
docker compose up -d
```

3. Access the application in your browser:
```
http://localhost:8085
```

### Stopping the Application

```bash
docker compose down
```

## Usage

The Contacts Manager displays a table of business contacts with the following information:
- Name
- Email address
- Company
- Position
- Phone number

Click on any column header to sort the contacts by that field. The application will reload with the contacts sorted according to your selection.

## Technical Details

- **Backend**: PHP 8.2 with FPM
- **Web Server**: Nginx
- **Container**: Alpine Linux for minimal footprint
- **Port**: 8085 (configurable in docker-compose.yml)

## Project Structure

```
level-5/
├── docker-compose.yml    # Docker orchestration
├── Dockerfile           # Container configuration
├── nginx.conf          # Web server configuration
├── README.md          # This file
└── src/
    ├── index.php      # Main application
    └── styles.css     # Styling
```

## License

This project is provided as-is for educational and demonstration purposes.
