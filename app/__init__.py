from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # Configure upload folder
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Register blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app