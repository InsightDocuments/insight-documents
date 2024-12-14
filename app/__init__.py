from flask import Flask

def create_app():
    """
    Application factory function to initialize the Flask app.
    """
    app = Flask(__name__)

    # Register blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app