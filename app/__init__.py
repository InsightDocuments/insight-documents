from flask import Flask
from app.routes import main_bp

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(main_bp)
    
    return app