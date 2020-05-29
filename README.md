# building-restAPI-for-MLmodel-using-flask

### To install flask on ubuntu:
1. create a virtual environment on anaconda
```conda create -n flask_env python=3.7.7```
2. activate virtual environment
```conda activate flask_env```
3. install flask
```conda install flask```

If you want to see the version of flask
```flask --version```

The output I get is:
```
Python 3.7.7
Flask 1.1.2
Werkzeug 1.0.1
```

### Data
The data set can be downloaded from [here](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data/data)

### Model
Above data is used to train a regression model that predicts NYC Airbnb rental prices/costs.

### To Run this app locally:
#### To get the prediction in web browser:
Assuming you are already in flask_env; go to the directory containing app.py and run below in terminal
```
python app.py
```
Now open the web browser and run below URL of the API
```
http://127.0.0.1:5000/get_prediction?var[]=0&var[]=1&var[]=7192&var[]=5114&var[]=5022&var[]=1532&var[]=40.79851&var[]=-73.94399&var[]=10&var[]=15102&var[]=61&var[]=2&var[]=9&var[]=0.10&var[]=0
```
var[] contains values of features that are needed by the regression model to predict the price/cost.
You will see the output in web browser.

#### To get the prediction in terminal:
Assuming you are already in flask_env; go to the directory containing app_.py and run below in terminal
```
python app_.py
```
Now open another terminal and use HTTPie to make a GET request at the URL of the API
```
http http://127.0.0.1:5000/ query==[0,1,7192,5114,5022,1532,40.79851,-73.94399,10,15102,61,2,9,0.10,0]
```
you will see the value of prediction in the terminal as below:
```
HTTP/1.0 200 OK
Content-Length: 41
Content-Type: application/json
Date: Fri, 29 May 2020 10:52:55 GMT
Server: Werkzeug/1.0.1 Python/3.7.7

{
    "prediction": 163.11757587508328
}
```


