import chess
import random

def generate():
    board = chess.Board()

    def choose_move(board):
        legal_moves = list(board.legal_moves)
        try:
            move_index = random.randint(0, len(legal_moves)-1)

            return str(legal_moves[move_index])
        except:
            return 'No moves'
    
    num_moves = random.randint(1, 100)

    for _ in range(num_moves):
        chosen_move = choose_move(board)
        if chosen_move == 'No moves':
            break
        else:
            board.push_san(chosen_move)

    return board
