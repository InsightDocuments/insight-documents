from flask import Flask

def create_app():
    """Initialize the Flask application."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey123'

    # Import and register the main blueprint
    from .routes import main
    app.register_blueprint(main)

    return app