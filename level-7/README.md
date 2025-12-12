# Expression Validator

A professional web-based tool for testing and validating logical expressions.

## Features

- Clean, intuitive interface for expression testing
- Real-time validation of logical expressions
- Support for various expression types and operators
- Professional error handling and user feedback

## Requirements

- Docker
- Docker Compose

## Quick Start

1. Navigate to the project directory:
```bash
cd level-7
```

2. Build and start the application:
```bash
docker compose up -d
```

3. Access the application in your browser:
```
http://localhost:8007
```

## Usage

1. Enter a logical expression in the input field
2. Click "Validate Expression" to test it
3. View the validation result

### Example Expressions

- `1==1` - Tests equality
- `true` - Boolean value
- `'hello'=='hello'` - String comparison
- `5>3` - Numeric comparison

## Stopping the Application

```bash
docker compose down
```

## Technical Stack

- PHP 7.0
- Nginx
- Alpine Linux
- Docker

## License

For educational and professional use.
