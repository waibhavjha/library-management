import os
import sys

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

import requests
from app.auth import generate_token

# Base URL of your API
BASE_URL = 'http://localhost:5000/api'

# Generate token
token = generate_token("admin")

# Headers to use in all requests
headers = {
    'Authorization': token,
    'Content-Type': 'application/json'
}

# Example: Create a new book
def create_book():
    response = requests.post(
        f'{BASE_URL}/books/',
        headers=headers,
        json={
            'title': 'The Great Gatsby',
            'author': 'F. Scott Fitzgerald',
            'isbn': '9780743273565',
            'quantity': 5
        }
    )
    print('Create book response:', response.json())
    return response.json()

# Example: Get all books
def get_books():
    response = requests.get(
        f'{BASE_URL}/books/',
        headers=headers
    )
    print('Get books response:', response.json())

# Example: Search books
def search_books(query):
    response = requests.get(
        f'{BASE_URL}/books/?search={query}',
        headers=headers
    )
    print('Search books response:', response.json())

if __name__ == '__main__':
    # Run examples
    book = create_book()
    get_books()
    search_books('Gatsby') 