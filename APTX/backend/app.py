from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def api_status():
    return jsonify({"status": "Backend API werkt!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

