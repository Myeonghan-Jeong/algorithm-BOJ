# 2438(print) / print stars with left triangle shape
for i in range(int(input())):
    print('*' * (i + 1))


# 2439(print) / print stars with right triangle shape
num = int(input())

for i in range(1, num + 1):
    print(' ' * (num - i) + '*' * i)


# 2440(print) / print stars with reverse left triangle shape
for i in range(int(input()), 0, -1):
    print('*' * i)


# 2441(print) / print stars with reverse right triangle shape
N = int(input())

for i in range(N, 0, -1):
    print(' ' * (N - i) + '*' * i)


# 2442(print) / print stars with center triangle shape
N = int(input())

for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * (2 * i - 1))


# 2443(print) / print stars with reverse center triangle shape
N = int(input())

for i in range(N, 0, -1):
    print(' ' * (N - i) + '*' * (2 * i - 1))


# 2444(print) / print stars with diamond shape
N = int(input())

for i in range(1, 2 * N):
    if i <= N:
        print(' ' * (N - i) + '*' * (2 * i - 1))
    else:
        print(' ' * (i - N) + '*' * (4 * N - 2 * i - 1))
        