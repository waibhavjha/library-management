from flask import Flask
from config import Config
from typing import Optional

app: Optional[Flask] = None

def create_app(config_class=Config) -> Flask:
    global app
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize database (using simple file-based storage for this example)
    from app.models import init_db
    init_db()
    
    # Register blueprints
    from app.routes.books import bp as books_bp
    from app.routes.members import bp as members_bp
    
    app.register_blueprint(books_bp, url_prefix='/api/books')
    app.register_blueprint(members_bp, url_prefix='/api/members')
    
    return app 