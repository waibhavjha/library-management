import os
import sys
sys.path.append(os.getcwd())

from app.auth import generate_token

def main():
    # Generate token for admin user
    token = generate_token("admin")
    
    print("\nYour authentication token:")
    print("-" * 50)
    print(token)
    print("-" * 50)
    
    print("\nExample usage with curl:")
    print(f'curl -X GET http://localhost:5000/api/books/ -H "Authorization: {token}"')
    
    print("\nExample usage with Python requests:")
    print("""
import requests

headers = {
    'Authorization': '""" + token + """',
    'Content-Type': 'application/json'
}

response = requests.get('http://localhost:5000/api/books/', headers=headers)
print(response.json())
    """)

if __name__ == "__main__":
    main() 