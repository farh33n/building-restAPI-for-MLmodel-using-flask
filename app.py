from model import Model
from flask import Flask, request
import joblib
import numpy as np

app = Flask(__name__)

reg_model = Model()

model_path = 'model/reg_model.pkl'
with open(model_path, 'rb') as f:
    reg_model.reg = joblib.load(f)

@app.route('/get_prediction', methods=['GET'])
def get_prediction():
    data = request.args.getlist('var[]', type=float)
    type1 = type(data)
    data = np.array(data, dtype=np.float32)
    type2 = type(data)
    data = np.reshape(data, (1, -1))
    prediction = reg_model.predict(data)
    # create JSON object
    output = {'prediction': prediction}

    #return output
    return '''<h1>features passed as parameters are: {}</h1>
              <h1>The predicted value is: {}'''.format(data, output)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
