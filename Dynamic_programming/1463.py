# 1463 / calculate min of using the lowest calculation
info = {1: 0, 2: 1}


def find(n):  # set function with DP

    if n in info:  # check number is in dict
        return info[n]

    # find min number of calculation
    # n // k: number of divison calculation
    # n % k: number of minus calculation
    m = 1 + min(find(n // 2) + n % 2, find(n // 3) + n % 3)
    info[n] = m  # add result to dict

    return m


N = int(input())
print(find(N))
