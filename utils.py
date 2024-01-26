import platform
import chess.engine

def string_to_data(file="",board=""):
    if file != "":
        with open(file, "r") as file:
            content = file.read()
            rows = content.split("\n")
            data=[]
            for row in rows[0:10_000]:
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
def decode(data):
    pieces = {
        0 : ".",
        100 : "K",
        1 : "P",
        3 : "N",
        3.5 : "B",
        5 : "R",
        9 : "Q"
    }
    decoded = ""
    for i in range(1, len(data)+1):
        p = pieces[abs(float(data[i-1]))]
        decoded += p if i >= 0 else p.lower()
        if i % 8 == 0:
            decoded += "\n"
        else:
            decoded += " "
    return decoded

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
    