import numpy as np
import json

def flat_list(line):
    res = []
    for row in line:
        res.extend(row)
    return res 

def task1(line):    
    line = json.loads(line)
    used = []
    res = np.zeros((len(flat_list(line)), len(flat_list(line))))    
    for elx in line:
        for x in elx:
            for ely in line:
                for y in ely:
                    if y not in flat_list(used):    
                        res[int(x) - 1][int(y) - 1] = 1
        used.append(elx)
    return res

def task2(line_1, line_2):
    res_1 = task1(line_1)
    res_2 = task1(line_2)
    res = np.ones((len(res_1[0]), len(res_1[0])))
    for i in range(len(res_1[0]) - 1):
        if res_1[i + 1][i] != res_2[i + 1][i] and res_1[i][i + 1] != res_2[i][i + 1]:
            res[i + 1][i] = 0
            res[i][i + 1] = 0            
    return res

def task(line_1, line_2):
    res = task2(line_1, line_2)
    ind_list = []
    res_list = []
    i = 0
    while i  < len(res[0]):
        if res[i][i - 1] == 0:
            ind_list.pop(-1)
            ind_list.append([str(i), str(i + 1)])
        else: 
            ind_list.append(str(i + 1))
        i += 1
    return json.dumps(ind_list)
if __name__ == "__main__":
    print(task('[["1","2"],["3","4","5"],"6","7","9",["8","10"]]','["1",["2","3"],"4",["5","6","7"],"8","9","10"]'))