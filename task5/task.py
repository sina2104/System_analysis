import numpy as np

def task1(line):
    ind_line, flat_line = [], []
    pos = 0
    for el in line:
        if isinstance(el, int):
            el = [el]
        for val in el:
            ind_line.append(pos)
            flat_line.append(val)
        pos += 1       
    res = [[0 for _ in range(len(flat_line))] for _ in range(len(flat_line))]

    for i in range(len(ind_line)):
        for j in range(len(ind_line)):
            if ind_line[flat_line.index(j + 1)] >= ind_line[flat_line.index(i + 1)]:
                res[i][j] = 1
   
    return res

def task2(line_1, line_2):
    line_1 = task1(line_1)
    line_2 = task1(line_2)

    line_1_trans = np.transpose(line_1)
    line_2_trans = np.transpose(line_2)
    res_1 = np.zeros((len(line_1_trans), len(line_1_trans)))
    res_2 = np.zeros((len(line_1_trans), len(line_1_trans)))    
    res = np.zeros((len(line_1_trans), len(line_1_trans)))
    res_0 = []
    for i in range(len(line_1_trans)):
        for j in range(len(line_1_trans)):
            res_1[i][j] = line_1[i][j] * line_2[i][j]
            res_2[i][j] = line_1_trans[i][j] * line_2_trans[i][j]
            res[i][j] = res_1[i][j] or res_2[i][j]
            if res[i][j] == 0 and [j + 1, i + 1] not in res_0:
                res_0.append([i + 1, j + 1])
    return res_0


def task(line_1, line_2, res_0):
    res = []

    for i, ex1 in enumerate(line_1):
        line_1_set = set(ex1) if isinstance(ex1, list) else set([ex1])
        
        for j, ex2 in enumerate(line_2):
            line_2_set = set(ex2) if isinstance(ex2, list) else set([ex2])

            for val in line_1_set:
                for el in res_0:
                    if val in el and el not in res:
                        res.append(el)
                        break

            inter = line_1_set.intersection(line_2_set)
            if inter and not any(val in el for el in res_0):
                res.append(list(inter) if len(inter) > 1 else inter.pop())

    return res

if __name__ == "__main__":
    line_1 = [1,[2,3],4,[5,6,7],8,9,10]
    line_2 = [[1,2],[3,4,5],6,7,9,[8,10]]

    print(task(line_1, line_2, task2(line_1, line_2)))
