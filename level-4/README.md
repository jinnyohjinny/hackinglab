# Greeting Service

A simple web application that provides personalized greeting messages.

## Features

- Clean, modern web interface
- Personalized greeting generation
- Responsive Bootstrap design

## Requirements

- Docker
- Docker Compose

## Quick Start

1. Navigate to the project directory:
   ```bash
   cd level-4
   ```

2. Build and run the application using Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Open your browser and visit:
   ```
   http://localhost:5000
   ```

4. Enter your name in the form to receive a personalized greeting!

## Usage

You can also access the greeting service directly via URL parameters:
```
http://localhost:5000/?name=John
```

## Stopping the Application

Press `Ctrl+C` in the terminal where docker-compose is running, or run:
```bash
docker-compose down
```

## Technology Stack

- Python 3.11
- Flask 3.0.0
- Bootstrap 5.3.0
- Docker & Docker Compose
