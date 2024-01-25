from generate_board import generate
import chess.engine
import utils

boards = []

for i in range(10000):
    boards.append(generate())
    print(f'Board {i+1} generated')


engine = chess.engine.SimpleEngine.popen_uci('./stockfish-ubuntu-x86-64-avx2')

def analyse(board):
    info = engine.analyse(board, limit=chess.engine.Limit(depth=16))
    print('Analysed')

    return info['score'].relative.score(mate_score=100_000)/100
    
evals = [analyse(board) for board in boards]
engine.quit()

encoded_boards = [utils.encode(board) for board in boards]

data = open('data.txt', 'w')

for board in range(len(encoded_boards)):
    data.write(str(encoded_boards[board]) + f' {evals[board]}\n')

data.close()