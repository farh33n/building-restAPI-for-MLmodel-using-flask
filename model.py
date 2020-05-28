from sklearn.linear_model import LinearRegression

class Model(object):

    def __init__(self):
        self.reg = LinearRegression()

    def train(self, X, y):
        """Trains the regression model
        """
        self.reg.fit(X, y)

    def predict(self, X):
        """Returns the predicted value
        """
        y_pred = self.reg.predict(X)
        return y_pred
