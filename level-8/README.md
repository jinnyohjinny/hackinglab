# Data Analytics Platform

A professional enterprise-grade data processing and analytics platform built with Ruby and Sinatra.

## Features

- 🔐 **Secure Authentication** - User login and session management
- 📊 **Real-time Analytics** - Live dashboard with key metrics
- 📁 **Data Upload** - Support for CSV, JSON, and XML files
- 🔍 **Query Builder** - Execute custom data queries
- 📋 **Activity Logging** - Comprehensive system activity tracking
- 🎨 **Modern UI** - Clean, professional interface with dark theme

## Quick Start

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone this repository
2. Navigate to the project directory
3. Start the application:

```bash
docker compose up -d
```

The application will be available at `http://localhost:3000`

### Demo Accounts

- **Admin**: `admin` / `admin123`
- **Analyst**: `analyst` / `analyst456`
- **Demo**: `demo` / `demo789`

## Usage

1. **Login**: Use one of the demo accounts to access the platform
2. **Dashboard**: View real-time analytics and system metrics
3. **Upload Data**: Upload CSV, JSON, or XML files for processing
4. **Run Queries**: Use the query builder to analyze your data
5. **Monitor Activity**: Check the activity logs for system events

## Technology Stack

- **Backend**: Ruby 2.7 with Sinatra
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Server**: Puma
- **Containerization**: Docker

## API Endpoints

- `POST /api/login` - User authentication
- `POST /api/logout` - User logout
- `GET /api/session` - Check session status
- `GET /api/analytics` - Retrieve analytics data
- `POST /api/upload` - Upload data files
- `POST /api/query` - Execute data queries
- `GET /api/logs` - Retrieve activity logs

## Development

To run in development mode:

```bash
bundle install
ruby app.rb
```

## Security

This application implements industry-standard security practices including:
- Session-based authentication
- Input validation and sanitization
- Secure error handling
- Production-ready configuration

## License

For educational and research purposes only.
