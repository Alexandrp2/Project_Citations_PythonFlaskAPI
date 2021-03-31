from flask import Flask, request, Response, jsonify, json
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.json_util import dumps
from bson import ObjectId
import re

'''
Pour la gestion du CORS
pip install -U flask-cors
'''

app = Flask(__name__)

# Autorise le CORS pour toute l'application (toutes les routes)
CORS(app)

# Configuration pour utilisation d'une base MongoDB locale ou distante (sur le cloud MongoDB Atlas)
app.config['MONGO_URI'] = "mongodb://localhost:27017/citations-app"
# app.config['MONGO_URI'] = "mongodb+srv://citationDbUser:citationDbPassword@cluster0.ooo2r.mongodb.net/citations-app?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def test():
    return Response(response=json.dumps({"Status": "UP"}),
                    status=200,
                    mimetype='application/json')


'''

ROUTES CITATIONS

'''


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


@app.route('/citations/auteur/<auteur>', methods=['POST'])
def getCitationsByAuthor(auteur):
    #citations = mongo.db.citations.find({"author":{"$regex": '/aPollinaiRE/', "$options" :'i'}})
    citations = mongo.db.citations.find({"author": "Guillaume Apollinaire"})
    response = dumps(citations)
    return Response(response,
                    status=200,
                    mimetype='application/json')

'''

ROUTES MON ESPACE

'''




'''

ROUTES STATISTIQUES

'''



if __name__ == "__main__":
    app.run(debug=True)