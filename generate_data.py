from generate_board import generate

boards = []

for _ in range(1000):
    try:
        boards.append(generate())
    except:
        boards.append(generate()) # Because bugs out for certain position