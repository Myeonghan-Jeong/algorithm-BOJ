# 2748 / calculate fibonachi`s number with DP
num = {0: 0, 1: 1, 2: 1}


def fibo(n):
    global num

    if n not in num:
        num[n] = fibo(n - 1) + fibo(n - 2)

    return num[n]


print(fibo(int(input())))
