from flask import Flask,request,render_template
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import jsonpickle
import json

app = Flask(__name__)

model = joblib.load('rfr_model.joblib')

@app.route('/')
def hello_world():
    return render_template('form.html')

@app.route('/name')
def temp():
    return 'dfsdfsdfdsf'

@app.route('/test')
def test():
    input1 = pd.read_csv("test.csv")
    print(input1)
    prediction = model.predict(input1)
    print(input1)
    print(prediction)
    return ' '.join([str(elem) for i,elem in enumerate(prediction)])

@app.route('/predict', methods=['POST'])
def predict():
    # data = request.get_json() 
    # name = data['name'] 
    # return f"Hello, {name}!"
    data = request.data.decode('utf-8')
    jin = json.loads(data)
    prediction = model.predict(pd.DataFrame(jin))
    return ' '.join([str(elem) for i,elem in enumerate(prediction)])
