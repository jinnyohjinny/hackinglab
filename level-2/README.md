# InfoManager

A secure information management system built with Flask.

## Features

- User authentication with secure password hashing
- Personal information storage and management
- Clean, responsive Bootstrap UI
- SQLite database for easy deployment

## Quick Start

### Using Docker Compose (Recommended)

1. Start the application:
```bash
docker-compose up -d
```

2. Access the application at `http://localhost:5000`

3. Stop the application:
```bash
docker-compose down
```

### Using Docker

1. Build the Docker image:
```bash
docker build -t infomanager .
```

2. Run the container:
```bash
docker run -p 5000:5000 infomanager
```

3. Access the application at `http://localhost:5000`

### Manual Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Access the application at `http://localhost:5000`

## Demo Accounts

The application comes pre-populated with demo accounts:

- **Username:** alice | **Password:** password123
- **Username:** bob | **Password:** securepass456

## Technology Stack

- **Backend:** Python 3.11, Flask 3.0
- **Database:** SQLite
- **Frontend:** Bootstrap 5.3, HTML5
- **Security:** SHA-256 password hashing

## Project Structure

```
level-2/
├── app.py                 # Main application file
├── templates/             # HTML templates
│   ├── login.html
│   ├── dashboard.html
│   └── info.html
├── static/                # Static assets
│   └── css/
│       └── style.css
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
└── README.md             # This file
```

## License

This project is for educational purposes only.
