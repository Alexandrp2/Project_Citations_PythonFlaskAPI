from flask import Flask, request, Response, jsonify, json
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson import ObjectId
'''
from flask_pymongo import PyMongo
from bson.json_util import dumps
from flask import Flask, Response,json,request

pip install -U flask-cors

app = Flask(__name__)
CORS(app)

'''

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/citations-app"

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def test():
    return Response(response=json.dumps({"Status": "UP"}),
                    status=200,
                    mimetype='application/json')


@app.route('/citations', methods=['GET'])
def getAllCitations():
    citations = mongo.db.citations.find({})
    response = dumps(citations)
    return Response(response,
                    status=200,
                    mimetype='application/json')


@app.route('/citation/id/<id>', methods=['GET'])
def getCitationById(id):
    citation = mongo.db.citations.find_one({'_id':ObjectId(id)})
    response = dumps(citation)
    return Response(response,
                    status=200,
                    mimetype='application/json')


if __name__ == "__main__":
    app.run(debug=True)