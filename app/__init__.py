from flask import Flask
import os

def create_app():
    """
    Application factory to create and configure the Flask app.
    """
    app = Flask(__name__)

    # Set the upload folder path
    UPLOAD_FOLDER = os.path.join(app.root_path, 'uploads')
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # Import and register routes as a blueprint
    from .routes import app as routes_app
    app.register_blueprint(routes_app)

    return app