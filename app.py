from flask import Flask, jsonify, request
from waitress import serve


app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'message': 'Remote VM execution'})

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
