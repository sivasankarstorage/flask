from flask import Flask,request,render_template,make_response, send_file
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import jsonpickle
import json
# import csv
# import requests

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

# @app.route('/get_csv')
# def get_csv():
#     # Get data as an array of dictionaries
#     # data = [
#     #     {'name': 'John Doe', 'age': 30, 'email': 'john.doe@example.com'},
#     #     {'name': 'Jane Smith', 'age': 25, 'email': 'jane.smith@example.com'},
#     #     {'name': 'Bob Johnson', 'age': 40, 'email': 'bob.johnson@example.com'}
#     # ]
#     data = requests.get('https://ap-south-1.aws.data.mongodb-api.com/app/application-0-bgguv/endpoint/getCSV').text
#     print(type(data))
#     temp = json.loads(data)
#     # Convert data to CSV format
#     # print(temp)
#     fieldnames = ["discount", "approver", "days","status"]
#     csv_string = ",".join(fieldnames) + "\n"
#     print(temp[0]['discount'])
#     for item in temp:
#         print(item['discount'])
#         csv_string += ",".join([str(item[field]['$numberDouble']) for field in fieldnames]) + "\n"

#     # Send CSV data as response
#     response = make_response(csv_string)
#     response.headers.set('Content-Type', 'text/csv')
#     response.headers.set('Content-Disposition', 'attachment', filename='data.csv')

#     return response
