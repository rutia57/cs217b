import sys
sys.path.append('../')

from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from process_text import SpacyDocument

app = Flask(__name__)
api = Api(app)

app.config['JSON_SORT_KEYS'] = False

class NER(Resource):

    def get(self):
        return jsonify('This service performs Named Entity ' + \
                       'Recognition (NER) on the text that ' + \
                       'is provided (either as a .txt file ' + \
                       'using -d@<filename.txt>, or as a st' + \
                       'ring using -d \'<text to analyze>\').')

    def post(self):
        text = request.get_data(as_text=True)
        doc = SpacyDocument(text)
        entities = {'entities':[{
                                 'text' : e[3],
                                 'label': e[2],
                                 'span' : (e[0], e[1])
                                }
                                for e in doc.get_entities()]}
        return jsonify(entities)

api.add_resource(NER, '/api')

if __name__ == '__main__':
    app.run(debug=True)
