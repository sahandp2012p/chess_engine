from generate_board import generate
import chess.engine

boards = []

for _ in range(100):
    try:
        boards.append(generate())
    except:
        boards.append(generate()) # Because bugs out for certain position

engine = chess.engine.SimpleEngine.popen_uci('./stockfish-ubuntu-x86-64-avx2')

def analyse(board):
    info = engine.analyse(board, limit=chess.engine.Limit(depth=20))

    return info['score'].relative.score(mate_score=100000)
    
evals = [analyse(board) for board in boards]
engine.quit()