import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'HEAD'])
def serve_followers():
    data = {
        "frames": [
            {"text": "Followers: 4603", "icon": None}
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
