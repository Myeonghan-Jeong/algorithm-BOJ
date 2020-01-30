# 4948 / finc primes in N to 2N
primes = [0] * 123457 * 2
primes[0], primes[1] = 1, 1
for i in range(2, 123456 * 2):
    num = 2 * i
    while num <= 123456 * 2:
        primes[num] = 1
        num += i

while True:
    N = int(input())
    if N == 0:
        break

    cnt = 0
    for i in range(N + 1, 2 * N + 1):
        if primes[i] == 0:
            cnt += 1

    print(cnt)
