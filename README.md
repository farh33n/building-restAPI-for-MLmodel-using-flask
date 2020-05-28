# building-restAPI-for-MLmodel-using-flask

### To install flask on ubuntu:
1. create a virtual environment on anaconda
> conda create -n flask_env python=3.7.7
2. activate virtual environment
> conda activate flask_env
3. install flask
> conda install flask

If you want to see the version of flask
> flask --version

The output I get is:
```
Python 3.7.7
Flask 1.1.2
Werkzeug 1.0.1
```

### Data
The data set can be downloaded from [here](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data/data)

### To Run this app:
assuming you are already in flask_env, run below in terminal
```
python app.py
```
Now open the web browser and run below url
```
http://127.0.0.1:5000/get_prediction?var[]=0&var[]=1&var[]=7192&var[]=5114&var[]=5022&var[]=1532&var[]=40.79851&var[]=-73.94399&var[]=10&var[]=15102&var[]=61&var[]=2&var[]=9&var[]=0.10&var[]=0
```
var[] contains values of features that are needed by the regression model to predict the cost.

