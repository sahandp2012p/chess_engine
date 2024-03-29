import platform
import chess.engine

def decode(file="",board=""):
    if file != "":
        with open(file, "r") as file:
            content = file.read()
            rows = content.split("\n")
            data=[]
            for row in rows:
                if row == "": continue
                start_index = row.find('[')
                end_index = row.find(']')
                array_string = row[start_index:end_index+1]
                values = array_string[1:-1].split(',')
                data_list = [float(value.strip()) for value in values]
                score = float(row[end_index+1::])
                data.append((data_list, score))
            return data
    if board != "":
        start_index = board.find('[')
        end_index = board.find(']')
        array_string = row[start_index:end_index+1]
        values = array_string[1:-1].split(',')
        data_list = [float(value.strip()) for value in values]
        score = float(row[end_index+1::])
        return (data_list, score)
    return []

def encode(board):
    str_board = str(board).replace(' ', '').replace('\n', '')
    encoded_board = []
    
    for piece in str_board:
        if piece == '.':
            encoded_board.append(0)
        elif piece == 'K':
            encoded_board.append(100)
        elif piece == 'P':
            encoded_board.append(1)
        elif piece == 'N':
            encoded_board.append(3)
        elif piece == 'B':
            encoded_board.append(3.5)
        elif piece == 'R':
            encoded_board.append(5)
        elif piece == 'Q':
            encoded_board.append(9)
        elif piece == 'k':
            encoded_board.append(-100)
        elif piece == 'p':
            encoded_board.append(-1)
        elif piece == 'n':
            encoded_board.append(-3)
        elif piece == 'b':
            encoded_board.append(-3.5)
        elif piece == 'r':
            encoded_board.append(-5)
        elif piece == 'q':
            encoded_board.append(-9)
        
    return encoded_board

def fishy():
    if "macos" in platform.platform().lower():
        return chess.engine.SimpleEngine.popen_uci('./stockfish-macos-x86-64-modern')
    return chess.engine.SimpleEngine.popen_uci('./stockfish-ubuntu-x86-64-avx2')
    