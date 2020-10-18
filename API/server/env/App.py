from flask import Flask, jsonify
from flask_cors import CORS

from legislator import Legislator as leg
from RSSFeed import RSSFeedMain as rsfm 

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
    return leg.parseLegislator("legislators-current.csv")

@app.route('/getBills', methods=['GET'])
def get_bills():
    billMaker = rsfm()
    return billMaker.convertToJson()


if __name__ == '__main__':
    app.run()