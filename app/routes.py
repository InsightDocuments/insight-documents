from flask import Blueprint, render_template

# Create a Blueprint for modular routing
main = Blueprint('main', __name__)

@main.route('/')
def home():
    """Render the homepage with the upload and search UI."""
    return render_template('index.html')

from flask import request, redirect, url_for, flash
import os

# Configure upload folder and allowed file extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'pdf'}
main.config = {}
main.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    """Check if the uploaded file has a valid extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads."""
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('main.home'))
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('main.home'))
    
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(main.config['UPLOAD_FOLDER'], filename))
        flash('File uploaded successfully')
        return redirect(url_for('main.home'))
    else:
        flash('Invalid file type. Only PDFs are allowed.')
        return redirect(url_for('main.home'))