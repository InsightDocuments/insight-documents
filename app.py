from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "InsightDocuments MVP is running!"

if __name__ == "__main__":
    app.run(debug=True)