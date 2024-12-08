from flask import Flask, jsonify, request
import requests
import pandas as pd

app = Flask(__name__)

API_VERSION = "1.0.0"

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Dummy Web API!"})

@app.route('/api/data', methods=['GET'])
def get_data():
    data = pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["Item 1", "Item 2", "Item 3"],
        "description": ["This is item 1", "This is item 2", "This is item 3"]
    })
    return jsonify(data.to_dict(orient="records"))

@app.route('/api/data', methods=['POST'])
def post_data():
    incoming_data = request.json
    return jsonify({"received_data": incoming_data, "status": "success"}), 201

@app.route('/api/version', methods=['GET'])
def get_version():
    return jsonify({"api_version": API_VERSION})

@app.route('/api/external', methods=['GET'])
def external_api():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return jsonify({"external_data": response.json()})
    return jsonify({"error": "Failed to fetch external data"}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

