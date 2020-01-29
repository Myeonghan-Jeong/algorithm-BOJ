# 1929 / find primes in M to N
primes = [0] * 1000001  # eratostenes`s seele
primes[0], primes[1] = 1, 1
for i in range(2, 1000001):
    num = 2 * i
    while num <= 1000000:
        primes[num] = 1
        num += i

M, N = map(int, input().split())

for i in range(M, N + 1):
    if primes[i] == 0:
        print(i)
