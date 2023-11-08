import numpy as np

def task():
    amount = 6
    res = np.zeros((amount * 2 + 1, amount ** 2 + 1))
    for i in range(1, amount + 1):
        for j in range(1, amount + 1):
            res[i + j, i * j] += 1
    res /= 36

    HA_sum = np.sum(res, axis=1)
    HA_sum = HA_sum[HA_sum != 0]
    HA = -np.sum(HA_sum * np.log2(HA_sum))

    HB_sum = np.sum(res, axis=0)
    HB_sum = HB_sum[HB_sum != 0]
    HB = -np.sum(HB_sum * np.log2(HB_sum))

    res = res[res != 0]
    HAB = -np.sum(res * np.log2(res))

    HaB = HAB - HA

    I = HB - HaB

    ret = [HAB, HA, HB, HaB, I]
    return [round(el, 2) for el in ret]

if __name__ == "__main__":
    print(task())