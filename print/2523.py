# 2523 / print stars with found rule
N = int(input())
for i in range(1, 2 * N):
    if i <= N:
        print('*' * i)
    else:
        print('*' * (2 * N - i))
