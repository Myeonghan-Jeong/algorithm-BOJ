# 2581 / calculate sum of primes and the minest prime from M to N
primes = [0] * 10001  # find primes under 10000
primes[0], primes[1] = 1, 1
for i in range(2, 1001):
    num = 2 * i
    while num <= 10000:
        primes[num] = 1
        num += i

M, N = int(input()), int(input())

least, sco = float('inf'), 0
for i in range(M, N + 1):  # calculate primes in M to N
    if primes[i] == 0:
        sco += i
        least = min(least, i)

if least == float('inf'):
    print(-1)
else:
    print(sco)
    print(least)
