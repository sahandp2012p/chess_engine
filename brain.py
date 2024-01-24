import numpy as np
from sklearn.linear_model import LinearRegression
import utils
import chess

def predict(board)->float:
    data = utils.decode()
    X = np.array([i for i in data[0]])
    y = np.array([i for i in data[1]])
    model = LinearRegression()
    model.fit(X, y)

    model.predict()

predict(utils.encode(chess.Board()))