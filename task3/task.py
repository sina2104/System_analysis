from math import log

def Entropy(csv_line):
    matrix = []
    for row in csv_line.splitlines():
        row_ = []
        for val in row.split(","):
            row_.append(int(val))
        matrix.append(row_)

    entropy = 0
    for row in matrix:
        entropy_ = 0
        for val in row:
            p = val / (len(matrix) - 1)
            if p <= 0:
                continue
            log_ = log(p, 2)
            entropy_ += p * log_
        entropy += -entropy_

    print(entropy)

Entropy("2,0,2,0,0\n0,1,0,0,1\n2,1,0,0,1\n0,1,0,1,1\n0,1,0,1,1")
