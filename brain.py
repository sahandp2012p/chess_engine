import numpy as np
from sklearn.linear_model import LinearRegression
import utils
import chess

def predict(board)->float:
    data = utils.decode(file="data.txt")
    print(data[0])
    '''x = [i for i in data[0]]
    print(x)
    y = np.array([i for i in data[1]])
    model = LinearRegression()
    model.fit(x, y)

    model.predict()'''

a = predict(utils.encode(chess.Board()))
print(a)