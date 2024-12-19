import requests

# Your generated token
TOKEN = "admin:1734602904:06d195eb36f4a6b5db3ad6d6b7c01c5f757ddaf7d4d9b6a76079d72745ef39f7"

# Headers for all requests
headers = {
    'Authorization': TOKEN,
    'Content-Type': 'application/json'
}

# Base URL
BASE_URL = 'http://localhost:5000/api'

def test_api():
    try:
        # 1. Create a book
        print("\nCreating a book...")
        create_response = requests.post(
            f'{BASE_URL}/books/',
            headers=headers,
            json={
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'isbn': '9780743273565',
                'quantity': 5
            }
        )
        print("Response:", create_response.json())

        # 2. Get all books
        print("\nGetting all books...")
        get_response = requests.get(
            f'{BASE_URL}/books/',
            headers=headers
        )
        print("Response:", get_response.json())

    except requests.exceptions.ConnectionError:
        print("\nError: Could not connect to the server.")
        print("Make sure the Flask application is running (flask run)")

if __name__ == "__main__":
    test_api() 