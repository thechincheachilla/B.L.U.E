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
# Map with key of legislators and their sponsored bills
def get_bills():
    billMaker = rsfm()
    return billMaker.convertToJson(billMaker.legisToBill)

@app.route('/getBillInfos', methods=['GET'])
# Map with key of bill ids connected to list of in order short title, long title, summary
def get_billInfo():
    billMaker = rsfm()
    return billMaker.convertToJson(billMaker.idToSummaries)

@app.route('/getBillSponsors', methods=['GET'])
# Map with key of bill ids connected to their sponsers
def get_sponserOfBill():
    billMaker = rsfm()
    return billMaker.convertToJson(billMaker.idToSponsor)

if __name__ == '__main__':
    app.run()