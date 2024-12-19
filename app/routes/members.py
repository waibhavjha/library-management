from flask import Blueprint, request, jsonify
from typing import Dict, List
from app.models import db, Member
from app.auth import require_auth

bp = Blueprint('members', __name__)

@bp.route('/', methods=['GET'])
@require_auth
def get_members():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    members = list(db.members.values())
    start = (page - 1) * per_page
    end = start + per_page
    
    return jsonify({
        'members': [member.to_dict() for member in members[start:end]],
        'total': len(members),
        'page': page,
        'per_page': per_page
    })

@bp.route('/<int:id>', methods=['GET'])
@require_auth
def get_member(id: int):
    member = db.members.get(id)
    if not member:
        return jsonify({'error': 'Member not found'}), 404
    return jsonify(member.to_dict())

@bp.route('/', methods=['POST'])
@require_auth
def create_member():
    data = request.get_json()
    
    required_fields = ['name', 'email']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    member = Member(
        id=db.next_member_id,
        name=data['name'],
        email=data['email']
    )
    
    db.members[member.id] = member
    db.next_member_id += 1
    db.save()
    
    return jsonify(member.to_dict()), 201

@bp.route('/<int:id>/borrow/<int:book_id>', methods=['POST'])
@require_auth
def borrow_book(id: int, book_id: int):
    member = db.members.get(id)
    if not member:
        return jsonify({'error': 'Member not found'}), 404
    
    book = db.books.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    
    if book.quantity <= 0:
        return jsonify({'error': 'Book not available'}), 400
    
    if book_id in member.borrowed_books:
        return jsonify({'error': 'Book already borrowed'}), 400
    
    book.quantity -= 1
    member.borrowed_books.append(book_id)
    db.save()
    
    return jsonify(member.to_dict())

@bp.route('/<int:id>/return/<int:book_id>', methods=['POST'])
@require_auth
def return_book(id: int, book_id: int):
    member = db.members.get(id)
    if not member:
        return jsonify({'error': 'Member not found'}), 404
    
    book = db.books.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    
    if book_id not in member.borrowed_books:
        return jsonify({'error': 'Book not borrowed by this member'}), 400
    
    book.quantity += 1
    member.borrowed_books.remove(book_id)
    db.save()
    
    return jsonify(member.to_dict()) 