from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database to store API keys
API_KEYS = {}

@app.route("/")
def home():
    return "Welcome to the API! Use the endpoints to generate an API key and fetch questions."

@app.route("/api/v1/candidate/", methods=["POST"])
def generate_api_key():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email_address")

    if not name or not email:
        return jsonify({"error": "Name and email_address are required"}), 400

    # Generate a mock API key (for simplicity)
    api_key = f"mock-api-key-for-{email}"
    API_KEYS[email] = api_key

    return jsonify({"api_key": api_key})

@app.route("/api/v1/download/questions", methods=["GET"])
def download_questions():
    api_key = request.headers.get("x-api-key")

    if not api_key or api_key not in API_KEYS.values():
        return jsonify({"error": "Invalid or missing API key"}), 401

    # Mock questions
    questions = [
        {"id": 1, "question": "What is Python?"},
        {"id": 2, "question": "Explain Flask framework."},
    ]

    return jsonify({"questions": questions})

if __name__ == "__main__":
    app.run(debug=True)
