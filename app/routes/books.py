from flask import Blueprint, request, jsonify
from typing import Dict, List, Optional
from app.models import db, Book
from app.auth import require_auth

bp = Blueprint('books', __name__)

@bp.route('/', methods=['GET'])
@require_auth
def get_books():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    search = request.args.get('search', '')
    
    books = list(db.books.values())
    
    if search:
        books = [
            book for book in books
            if search.lower() in book.title.lower() or 
               search.lower() in book.author.lower()
        ]
    
    start = (page - 1) * per_page
    end = start + per_page
    
    return jsonify({
        'books': [book.to_dict() for book in books[start:end]],
        'total': len(books),
        'page': page,
        'per_page': per_page
    })

@bp.route('/<int:id>', methods=['GET'])
@require_auth
def get_book(id: int):
    book = db.books.get(id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book.to_dict())

@bp.route('/', methods=['POST'])
@require_auth
def create_book():
    data = request.get_json()
    
    required_fields = ['title', 'author', 'isbn', 'quantity']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    book = Book(
        id=db.next_book_id,
        title=data['title'],
        author=data['author'],
        isbn=data['isbn'],
        quantity=data['quantity']
    )
    
    db.books[book.id] = book
    db.next_book_id += 1
    db.save()
    
    return jsonify(book.to_dict()), 201

@bp.route('/<int:id>', methods=['PUT'])
@require_auth
def update_book(id: int):
    book = db.books.get(id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    
    data = request.get_json()
    
    if 'title' in data:
        book.title = data['title']
    if 'author' in data:
        book.author = data['author']
    if 'isbn' in data:
        book.isbn = data['isbn']
    if 'quantity' in data:
        book.quantity = data['quantity']
    
    db.save()
    return jsonify(book.to_dict())

@bp.route('/<int:id>', methods=['DELETE'])
@require_auth
def delete_book(id: int):
    if id not in db.books:
        return jsonify({'error': 'Book not found'}), 404
    
    del db.books[id]
    db.save()
    return '', 204 