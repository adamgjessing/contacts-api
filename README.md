# Contacts API

A RESTful API built with Python, Flask and SQLite that manages contacts with full CRUD functionality.

## Endpoints

- `GET /contacts` - Return all contacts
- `GET /contacts/<id>` - Return a single contact
- `POST /contacts` - Create a new contact
- `PUT /contacts/<id>` - Update an existing contact
- `DELETE /contacts/<id>` - Delete a contact

## How it works
1. Flask receives HTTP requests and routes them to the correct function
2. Each function queries the SQLite database using SQL commands
3. Results are converted to JSON and returned with appropriate status codes

## Testing
Run the automated test suite with:
python3 test_api.py

## Skills Used
- Python
- Flask
- SQLite
- REST API design
- HTTP methods (GET, POST, PUT, DELETE)
- Automated testing
- Input validation
- Git & GitHub

## Note
contacts.db and __pycache__ are excluded via .gitignore
