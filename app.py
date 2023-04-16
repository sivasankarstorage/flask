from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Success123!'

@app.route('/name')
def temp():
    return 'dfsdfsdfdsf'
