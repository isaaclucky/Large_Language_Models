from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import sys,os
sys.path.append(os.path.abspath(os.path.join('../scripts/')))
from prep_data import preprocess
app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return {"response":"Please send data in post method"}
    def post(self):
        some_json = request.get_json()
        prep = preprocess(some_json)

        # document = 
        
        return {'preprocessed data': prep.get_final_template()}, 201

api.add_resource(Hello,'/')


if __name__ == '__main__':
    app.run(debug=True)