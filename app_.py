from model import Model
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import joblib
import numpy as np
import ast

app = Flask(__name__)
api = Api(app)

reg_model = Model()

model_path = 'model/reg_model.pkl'
with open(model_path, 'rb') as f:
    reg_model.reg = joblib.load(f)

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query', required=True, help="Please provide features values")


class PredictCost(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['query']
        # convert the str to list
        user_query = ast.literal_eval(user_query)

        # convert the user's query to numpy array and make a prediction
        user_query = np.array(user_query)
        user_query = np.reshape(user_query, (1, -1))
        prediction = reg_model.predict(user_query)

        # create JSON object
        output = {'prediction': prediction[0,0]}

        return output


# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictCost, '/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
