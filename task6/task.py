import numpy as np
import json


def task(first, second, third):    
    first = json.loads(first)
    second = json.loads(second)
    third = json.loads(third)

    n = len(first)
    res = [0, 0, 0]
    avg = 0
    desp = 0
    desp_max = 9 * (n ** 3 - n) / (12 * (n - 1))

    for i in range(n):
        res[i] += int(first[i][1])
        res[i] += int(second[i][1])
        res[i] += int(third[i][1])
        avg += res[i]
    avg /= n

    for el in res:
        desp += (el - avg) ** 2
    desp /= 2

    return desp / desp_max


if __name__ == "__main__":
    print(task(
    '["O1","O2","O3"]',
    '["O1","O3","O2"]',
    '["O1","O3","O2"]'))