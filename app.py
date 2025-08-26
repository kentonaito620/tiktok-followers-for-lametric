import os
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

@app.route('/', methods=['GET', 'HEAD'])
def serve_followers():
    data = {
        "frames": [
            {"text": "4603"}  # Removed "icon": null
        ]
    }

    if request.method == 'HEAD':
        return Response(status=200, mimetype='application/json')

    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
