
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Weatherly!"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Using port 5001 as per your request.
