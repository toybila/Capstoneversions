import numpy as np
from flask import Flask, request, jsonify, render_template
from argparse import ArgumentParser
import pickle

parser = ArgumentParser()
parser.add_argument("-m", "--model", dest="model", help="location of the pickle file")

filename = parser.parse_args().model

app = Flask(__name__)
model = pickle.load(open('filename', 'rb'))

@app.route('/')
def index():
    return "Network Intrusion Detection System"

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=8080)