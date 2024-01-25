import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor
import generate_board
import utils
import chess.engine


def predict(model, board) -> float:
    data = utils.decode(file='data.txt')
 
    X = [i[0] for i in data]
    y = [i[1] for i in data]

    model.fit(X, y)

    return model.predict([board])

board = generate_board.generate()

gb = predict(GradientBoostingRegressor(), utils.encode(board))
lr = predict(LinearRegression(), utils.encode(board))
stockfish = chess.engine.SimpleEngine.popen_uci('./stockfish-ubuntu-x86-64-avx2')
stockfish_eval = stockfish.analyse(board, limit=chess.engine.Limit(depth=16))['score'].relative.score(mate_score=100_000)/100

print('Gradient Boosting Evaluation:', gb[0])
print('Linear Regression Evaluation:', lr[0])
print('Stockfish Evaluation:', stockfish_eval)
print('Difference from Stockfish:')
print('Gradient Boosting: ', abs(gb[0]-stockfish_eval))
print('Linear Regression: ', abs(lr[0]-stockfish_eval))

stockfish.quit()