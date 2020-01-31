# 9020 / find min diff goldbach partition of n
primes = [0] * 10001
primes[0], primes[1] = 1, 1
for i in range(2, 10000):
    num = 2 * i
    while num <= 10000:
        primes[num] = 1
        num += i

for _ in range(int(input())):
    diff = n = int(input())

    a, b = 0, float('inf')
    for i in range(2, n + 1):
        if primes[i] == 0:
            if primes[n - i] == 0:
                if diff >= abs(n - 2 * i):  # check diff
                    diff = abs(n - 2 * i)
                    a, b = i, n - i
                else:
                    break

    print(min(a, b), max(a, b))
