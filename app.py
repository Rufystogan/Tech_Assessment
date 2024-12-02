from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import traceback

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

API_URL = "https://assessment.takafulbrunei.com/api/v1/download/questions"

@app.route("/api/v1/download/questions", methods=["GET"])
def fetch_questions():
    api_key = request.headers.get("x-api-key")

    if not api_key:
        return jsonify({"error": "API key is required in the headers"}), 401

    try:
        # Forward the request to the external API with the provided API key
        response = requests.get(API_URL, headers={"x-api-key": api_key})
        
        print(f"External API Response: {response.status_code} - {response.text}")  # Log the response for debugging

        # Check if the external API request was successful
        if response.status_code == 200:
            return jsonify(response.json())  # Return the questions from the external API
        else:
            return jsonify({"error": "Failed to fetch questions from external API"}), response.status_code

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {str(e)}")
        return jsonify({"error": f"Error occurred while fetching data from the external API: {str(e)}"}), 500

    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        print(traceback.format_exc())
        return jsonify({"error": "An unexpected error occurred. Please try again."}), 500

if __name__ == "__main__":
    app.run(debug=True)
