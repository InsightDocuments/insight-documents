from app import create_app

# Create the Flask application instance
app = create_app()

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)