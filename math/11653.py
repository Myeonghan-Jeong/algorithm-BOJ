# 11653 / print all prime factors of number N with ASC
N = int(input())
while N != 1:
    for n in range(2, N + 1):
        if N % n == 0:
            N //= n
            print(n)
            break
