# 10870 / calculate nth number in fibos
fibo = {0: 0, 1: 1}


def f(n):
    global fibo

    if n not in fibo:
        fibo[n] = f(n - 1) + f(n - 2)

    return fibo[n]


print(f(int(input())))
