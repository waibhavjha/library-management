import unittest
import json
from app import create_app
from app.models import db, init_db
from config import TestingConfig

class TestBooks(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()
        init_db()
        
        # Add test auth token
        self.headers = {'Authorization': 'test:0:valid_signature'}
    
    def test_create_book(self):
        response = self.client.post(
            '/api/books/',
            headers=self.headers,
            json={
                'title': 'Test Book',
                'author': 'Test Author',
                'isbn': '1234567890',
                'quantity': 5
            }
        )
        
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Test Book')
        self.assertEqual(data['quantity'], 5)
    
    def test_get_book(self):
        # First create a book
        book_response = self.client.post(
            '/api/books/',
            headers=self.headers,
            json={
                'title': 'Test Book',
                'author': 'Test Author',
                'isbn': '1234567890',
                'quantity': 5
            }
        )
        book_id = json.loads(book_response.data)['id']
        
        # Then get it
        response = self.client.get(
            f'/api/books/{book_id}',
            headers=self.headers
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Test Book')
    
    def test_search_books(self):
        # Create some books
        self.client.post(
            '/api/books/',
            headers=self.headers,
            json={
                'title': 'Python Programming',
                'author': 'John Doe',
                'isbn': '1234567890',
                'quantity': 5
            }
        )
        
        self.client.post(
            '/api/books/',
            headers=self.headers,
            json={
                'title': 'Java Programming',
                'author': 'Jane Smith',
                'isbn': '0987654321',
                'quantity': 3
            }
        )
        
        # Search for Python books
        response = self.client.get(
            '/api/books/?search=python',
            headers=self.headers
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data['books']), 1)
        self.assertEqual(data['books'][0]['title'], 'Python Programming')

if __name__ == '__main__':
    unittest.main() 