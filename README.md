# Library Management System API

A Flask-based REST API for managing a library system, including books and members management with borrowing functionality.

## Features

- CRUD operations for books and members
- Book borrowing and return functionality
- Search functionality for books by title or author
- Pagination support
- Token-based authentication
- Type hints throughout the codebase
- Unit tests

## Getting Started

### Prerequisites

- Python 3.7+
- Flask

### Installation

1. Clone the repository: 
bash
git clone https://github.com/waibhavjha/library-management.git
cd library-management


2. Create a virtual environment and activate it:
bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install dependencies:
bash
pip install -r requirements.txt


### Running the Application

1. Set the Flask application:
bash
export FLASK_APP=app # On Windows: set FLASK_APP=app
export FLASK_ENV=development # On Windows: set FLASK_ENV=development


2. Run the application:
bash
flask run


The API will be available at `http://localhost:5000`

### Running Tests

bash
python -m unittest discover tests


## API Endpoints

### Books

- `GET /api/books/` - List all books (with pagination)
- `GET /api/books/?search=query` - Search books by title or author
- `GET /api/books/<id>` - Get a specific book
- `POST /api/books/` - Create a new book
- `PUT /api/books/<id>` - Update a book
- `DELETE /api/books/<id>` - Delete a book

### Members

- `GET /api/members/` - List all members (with pagination)
- `GET /api/members/<id>` - Get a specific member
- `POST /api/members/` - Create a new member
- `POST /api/members/<id>/borrow/<book_id>` - Borrow a book
- `POST /api/members/<id>/return/<book_id>` - Return a book

## Design Choices

1. **Simple File-based Storage**: For simplicity, the application uses JSON file-based storage instead of a database. In a production environment, this should be replaced with a proper database.

2. **Token-based Authentication**: A simple HMAC-based token authentication system is implemented. In production, this should be replaced with a more robust solution like JWT.

3. **Type Hints**: The codebase uses Python type hints throughout to improve code readability and catch potential type-related errors early.

4. **Blueprint Structure**: The application uses Flask blueprints to organize routes logically by resource type.

## Limitations

1. The file-based storage system is not suitable for production use due to:
   - Lack of proper concurrent access handling
   - Poor scalability
   - No transaction support

2. The authentication system is basic and lacks:
   - User management
   - Token expiration
   - Refresh token mechanism

3. No rate limiting implemented

4. No proper logging system

## Future Improvements

1. Replace file-based storage with a proper database (e.g., PostgreSQL)
2. Implement proper JWT authentication
3. Add rate limiting
4. Add proper logging
5. Add more comprehensive test coverage
6. Add API documentation using Swagger/OpenAPI

This implementation provides a solid foundation for a library management system with the following features:
1. CRUD operations for books and members
2. Search functionality
3. Pagination
4. Token-based authentication
5. Type hints
6. Unit tests
7. Clean project structure
8. Detailed documentation

To use the API, you'll need to generate a token (you can use the generate_token function in the auth.py file) and include it in the Authorization header of your requests.

The code is organized in a modular way, making it easy to extend and maintain. The file-based storage system can be easily replaced with a proper database in a production environment.