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

def encode(board):
    str_board = str(board).replace(' ', '').replace('\n', '')
    encoded_board = []
    
    for piece in str_board:
        if piece == '.':
            encoded_board.append(0)
        elif piece == 'K':
            encoded_board.append(1)
        elif piece == 'P':
            encoded_board.append(2)
        elif piece == 'N':
            encoded_board.append(3)
        elif piece == 'B':
            encoded_board.append(4)
        elif piece == 'R':
            encoded_board.append(5)
        elif piece == 'Q':
            encoded_board.append(6)
        elif piece == 'k':
            encoded_board.append(-1)
        elif piece == 'p':
            encoded_board.append(-2)
        elif piece == 'n':
            encoded_board.append(-3)
        elif piece == 'b':
            encoded_board.append(-4)
        elif piece == 'r':
            encoded_board.append(-5)
        elif piece == 'q':
            encoded_board.append(-6)
        
    return encoded_board

encoded_boards = [encode(board) for board in boards]