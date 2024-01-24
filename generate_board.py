import chess
import random

def generate():
    board = chess.Board()

    def choose_move(board):
        legal_moves = list(board.legal_moves)
        move_index = random.randint(0, len(legal_moves)-1)

        return str(legal_moves[move_index])
    
    num_moves = random.randint(1, 100)

    for _ in range(num_moves):
        board.push_san(choose_move(board))

    return board
