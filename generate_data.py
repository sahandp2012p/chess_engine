from generate_board import generate
import chess.engine
import utils
from tqdm import tqdm



#engine = chess.engine.SimpleEngine.popen_uci('./stockfish-ubuntu-x86-64-avx2')
engine = chess.engine.SimpleEngine.popen_uci('./stockfish-macos-x86-64-modern')

DATA_COUNT = 10
boards = []
with tqdm(total=DATA_COUNT, ncols=80) as pbar:
    for i in range(DATA_COUNT):
        boards.append(generate())

        pbar.set_description("Generating")
        pbar.update(1)


def analyse(board):
    info = engine.analyse(board, limit=chess.engine.Limit(depth=16))

    return info['score'].relative.score(mate_score=100_000)/100

evals = []
with tqdm(total=len(boards), ncols=80) as pbar:
    for i in range(len(boards)):
        
        evals.append(analyse(boards[i]))
        pbar.set_description("Analysing")
        pbar.update(1)

engine.quit()

encoded_boards = [utils.encode(board) for board in boards]

data = open('data2.txt', 'w')

for board in range(len(encoded_boards)):
    encoded_data = encoded_boards[board]
    encoded_data.append(1 if boards[board].turn == True else 0) #add turn to data
    data.write(str(encoded_data) + f' {evals[board]}\n')

data.close()