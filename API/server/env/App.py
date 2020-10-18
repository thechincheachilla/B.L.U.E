from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import csv

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/getLegislators', methods=['GET'])
def get_legislators():
    raw = pd.read_csv("legislators-current.csv").T.to_dict()
    return jsonify(raw)


if __name__ == '__main__':
    app.run()