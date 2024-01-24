import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor
import generate_board
import utils
import chess

def linear_predict(board)->float:
    data = utils.decode(file="data.txt")
    X = [i[0] for i in data]
    y = [i[1] for i in data]
    model = LinearRegression()
    model.fit(X, y)
    return model.predict([board])

def gradient_predict(board)->float:
    training_data = utils.decode(file="data.txt")
    model = GradientBoostingRegressor()

    X = [i[0] for i in training_data]
    y = [i[1] for i in training_data]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(mean_squared_error(y_test, y_pred))


    

board = generate_board.generate()
a = linear_predict(utils.encode(chess.Board()))
print(a)