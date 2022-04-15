from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def hello():
    return "Message : Remote VM Execution !"

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
