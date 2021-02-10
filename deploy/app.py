import numpy as np
from flask import Flask, request, jsonify, render_template
from argparse import ArgumentParser
import pickle

parser = ArgumentParser()
parser.add_argument("-m", "--model", dest="model", help="location of the pickle file")

filename = parser.parse_args().model

app = Flask(__name__)
model = pickle.load(open(filename, 'rb'))

@app.route('/')
def index():
    return "Network Intrusion Detection System"



@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    Attackclasses = ['BENIGN', 'DDoS', 'PortScan', 'Bot', 'Infiltration', 'Web Attack � Brute Force', 'Web Attack � XSS','Web Attack � Sql Injection', 
                     'FTP-Patator', 'SSH-Patator', 'DoS slowloris', 'DoS Slowhttptest', 'DoS Hulk', 'DoS GoldenEye', 'Heartbleed']

    output = Attackclasses[int(prediction[0])]

    return jsonify(output)

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=8080)