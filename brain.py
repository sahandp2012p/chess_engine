import numpy as np
from sklearn.linear_model import LinearRegression
import utils
import chess

def predict(board)->float:
    data = utils.decode(file="data.txt")
    X = [i[0] for i in data]
    y = [i[1] for i in data]
    model = LinearRegression()
    model.fit(X, y)

    return model.predict([board])

a = predict(utils.encode(chess.Board()))
print(a)