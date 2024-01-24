import numpy as np
import statsmodels.api as sm

def decode():
    with open("data.txt", "r") as file:
        content = file.read()
        rows = content.split("\n")
        data=[]
        for row in rows:
            start_index = row.find('[')
            end_index = row.find(']')
            array_string = row[start_index:end_index+1]
            values = array_string[1:-1].split(',')
            data_list = [int(value.strip()) for value in values]
            score = int(row[end_index+1::])
            data.append((data_list, score))
        return data

def fit():
    data = decode()
    boards = [i for i in data[1]]
    scores = [i for i in data[0]]
    print(scores)
    sm.add_constant(boards)
    model = sm.OLS(scores, boards)
    results = model.fit()
    print(results.summary())