# 2438 / print stars with left triangle
for i in range(int(input())):
    print('*' * (i + 1))


# 2439 / print stars with right triangle
num = int(input())

for i in range(1, num + 1):
    print(' ' * (num - i) + '*' * i)


# 2440 / print stars with reverse left triangle
for i in range(int(input()), 0, -1):
    print('*' * i)


# 2441 / print stars with reverse right triangle
N = int(input())

for i in range(N, 0, -1):
    print(' ' * (N - i) + '*' * i)


# 2442 / print stars with center triangle
N = int(input())

for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * (2 * i - 1))


# 2443 / print stars with reverse center triangle
N = int(input())

for i in range(N, 0, -1):
    print(' ' * (N - i) + '*' * (2 * i - 1))


# 2444 / print stars with diamond
N = int(input())

for i in range(1, 2 * N):
    if i <= N:
        print(' ' * (N - i) + '*' * (2 * i - 1))
    else:
        print(' ' * (i - N) + '*' * (4 * N - 2 * i - 1))
