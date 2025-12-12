# Secure Profile Manager

A robust and secure user profile management application built with Flask and SQLAlchemy.

## Features
- Secure User Registration and Login
- User Dashboard
- Role-based Access Control (Admin Panel)
- Modern Bootstrap 5 UI

## Getting Started

### Prerequisites
- Docker

### Installation & Run
1. Build the Docker image:
   ```bash
   docker build -t secure-profile-app .
   ```

2. Run the application:
   ```bash
   docker run -p 5000:5000 secure-profile-app
   ```

3. Open your browser and navigate to `http://localhost:5000`

### Admin Access
The Admin Panel is restricted to authorized personnel only. Attempts to access it without proper credentials will be logged.

## Technology Stack
- **Backend:** Python, Flask, SQLAlchemy
- **Frontend:** HTML5, Bootstrap 5
- **Database:** SQLite
