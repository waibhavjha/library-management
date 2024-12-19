from typing import Dict, List, Optional
import json
import os
from datetime import datetime

class Book:
    def __init__(self, id: int, title: str, author: str, isbn: str, quantity: int):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity
    
    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'quantity': self.quantity
        }

class Member:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books: List[int] = []
    
    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'borrowed_books': self.borrowed_books
        }

# Simple file-based storage
class Database:
    def __init__(self):
        self.books: Dict[int, Book] = {}
        self.members: Dict[int, Member] = {}
        self.next_book_id: int = 1
        self.next_member_id: int = 1
        
    def save(self):
        data = {
            'books': {str(k): v.to_dict() for k, v in self.books.items()},
            'members': {str(k): v.to_dict() for k, v in self.members.items()},
            'next_book_id': self.next_book_id,
            'next_member_id': self.next_member_id
        }
        with open('database.json', 'w') as f:
            json.dump(data, f)
    
    def load(self):
        if not os.path.exists('database.json'):
            return
        
        with open('database.json', 'r') as f:
            data = json.load(f)
            
        self.books = {
            int(k): Book(**v) for k, v in data['books'].items()
        }
        self.members = {
            int(k): Member(**{k2: v2 for k2, v2 in v.items() if k2 != 'borrowed_books'})
            for k, v in data['members'].items()
        }
        for k, v in data['members'].items():
            self.members[int(k)].borrowed_books = v['borrowed_books']
            
        self.next_book_id = data['next_book_id']
        self.next_member_id = data['next_member_id']

db = Database()

def init_db():
    db.load() 