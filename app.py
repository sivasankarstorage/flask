from flask import Flask
import pandas as pd
import joblib
app = Flask(__name__)

model = joblib.load('rf_model.joblib')

@app.route('/')
def hello_world():
    return 'Hello, Success123!'

@app.route('/name')
def temp():
    return 'dfsdfsdfdsf'

@app.route('/test')
def test():
    input1 = pd.read_csv("test.csv")
    prediction = model.predict(input1)
    print(input1)
    print(prediction)
    return ' '.join([str(elem) for i,elem in enumerate(prediction)])
