import os
import sys
sys.path.append(os.getcwd())

from app.auth import generate_token
import requests
import json

def demonstrate_api_usage():
    # Generate token
    token = generate_token("admin")
    print("\nGenerated token:", token)

    # Setup headers
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    # Base URL
    base_url = 'http://localhost:5000/api'

    try:
        # 1. Create a book
        print("\n1. Creating a book...")
        create_response = requests.post(
            f'{base_url}/books/',
            headers=headers,
            json={
                'title': 'Test Book',
                'author': 'Test Author',
                'isbn': '1234567890',
                'quantity': 5
            }
        )
        print(json.dumps(create_response.json(), indent=2))

        # 2. Get all books
        print("\n2. Getting all books...")
        get_response = requests.get(
            f'{base_url}/books/',
            headers=headers
        )
        print(json.dumps(get_response.json(), indent=2))

    except requests.exceptions.ConnectionError:
        print("\nError: Could not connect to the server.")
        print("Make sure the Flask application is running (flask run)")

if __name__ == "__main__":
    demonstrate_api_usage() 