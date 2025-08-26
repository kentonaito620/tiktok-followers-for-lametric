import os
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

@app.route('/', methods=['GET', 'HEAD'])
def serve_followers():
    data = {
        "frames": [
            {"text": "Followers: 4603", "icon": None}
        ]
    }

    if request.method == 'HEAD':
        # Return headers only, no body
        return Response(status=200, mimetype='application/json')

    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
