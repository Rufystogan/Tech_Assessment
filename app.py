from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api-key', methods=['POST'])
def get_api_key():
    data = {
        "name": request.json.get("name"),
        "email_address": request.json.get("email_address")
    }
    response = requests.post("https://assessment.takafulbrunei.com/v1/candidate/", json=data)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
