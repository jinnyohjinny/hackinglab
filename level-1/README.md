# SecureApp

A modern web application with user authentication and role-based access control.

## Features

- User registration and authentication
- Secure session management
- Role-based access control
- Admin panel for user management
- Modern, responsive UI
- SQLite database

## Prerequisites

- Docker and Docker Compose installed on your system

## Quick Start

### Using Docker Compose (Recommended)

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd level-1
   ```

3. Build and start the application:
   ```bash
   docker-compose up --build
   ```

4. Access the application at `http://localhost:5000`

### Using Docker

1. Build the Docker image:
   ```bash
   docker build -t secureapp .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 secureapp
   ```

3. Access the application at `http://localhost:5000`

## Usage

### Registration

1. Navigate to `http://localhost:5000`
2. Click "Sign up" to create a new account
3. Fill in your username, email, and password
4. Click "Create Account"

### Login

1. Navigate to `http://localhost:5000`
2. Enter your username and password
3. Click "Sign In"

### Admin Access

An admin account is automatically created with the following credentials:
- **Username:** admin
- **Password:** admin123

The admin panel is accessible at `/admin` and provides:
- User management interface
- System statistics
- Administrative controls

## Project Structure

```
level-1/
├── src/
│   ├── app.py              # Main Flask application
│   ├── models.py           # Database models
│   ├── auth.py             # Authentication utilities
│   ├── static/
│   │   └── style.css       # Application styles
│   └── templates/
│       ├── login.html      # Login page
│       ├── register.html   # Registration page
│       ├── dashboard.html  # User dashboard
│       └── admin.html      # Admin panel
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose configuration
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Technology Stack

- **Backend:** Flask (Python)
- **Database:** SQLite with SQLAlchemy ORM
- **Frontend:** HTML5, CSS3
- **Containerization:** Docker

## Security Features

- Password hashing using Werkzeug
- Session-based authentication
- HTTP-only cookies
- Role-based access control
- Input validation

## Stopping the Application

### Docker Compose
```bash
docker-compose down
```

### Docker
```bash
docker stop secureapp
```

## Development

To run in development mode with live reload:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   cd src
   python app.py
   ```

## License

This project is provided as-is for educational purposes.
