from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def serve_json():
    return send_file('followers.json', mimetype='application/json')

if __name__ == '__main__':
    app.run()
