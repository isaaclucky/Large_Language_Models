from extract_entities import extract_entities
from prep_data import preprocess
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import sys
import os
sys.path.append(os.path.abspath(os.path.join('../scripts/')))

app = Flask(__name__)
api = Api(app)


class Entity_Extraction(Resource):
    def get(self):
        return {"response": "Please send data in post method"}

    def post(self):
        extract = extract_entities()
        some_json = request.get_json()
        if type(some_json) == list:
            result = []
            for i in some_json:
                result.append(extract.return_extracted(i))
            return result, 201
        else:
            result = extract.return_extracted(some_json)
            return result, 201


api.add_resource(Entity_Extraction, '/jdentities')


if __name__ == '__main__':
    app.run(debug=True)
