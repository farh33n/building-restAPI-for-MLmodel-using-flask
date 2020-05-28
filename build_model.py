'''
This module builds the model and saves it as well.
The primary focus of this project is using flask hence no attention has been paid to conversion of strings to integers;
most simple approach has been used for this purpose. I might update the code and improve that part in the future.
'''
from model import Model
import os
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib

def build_model():
    reg_model = Model()

    with open('data/AB_NYC_2019.csv') as f:
        data = pd.read_csv(f, sep=',')
    data = data.dropna()

    X = data[[data.columns.difference(['price'])]]
    y = data['price']

    obj_cols = X.select_dtypes(include=['object']).columns.tolist()
    for col in obj_cols:
        X[col] = X[col].astype('category')
    cat_cols = X.select_dtypes(include=['category']).columns.tolist()
    X[cat_cols] = X[cat_cols].apply(lambda x: x.cat.codes)

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    reg_model.train(X_train, y_train)

    os.makedirs("model", exist_ok=True)
    joblib.dump(value=reg_model, filename="model/reg_model.pkl")


if __name__ == "__main__":
    build_model()
