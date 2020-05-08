# 11401 / calculate nCk with Fermat's little theorem
def square(a, n):
    global p

    if n == 0:
        return 1
    elif n == a:
        return a
    elif n % 2 > 0:  # if n is odd
        return a * square(a, n - 1)
    else:  # if n is even
        t = square(a, n // 2)  # div 2
        t %= p  # calculate mod
        return t ** 2 % p  # multiple and mod


# fermat`s: A ** (p - 1) % p = 1, when a is number, p is prime
N, K = map(int, input().split())
A, B, p = 1, 1, 1000000007
for i in range(1, N + 1):  # calulate N!
    A *= i
    A %= p
for i in range(1, K + 1):  # calculate K!
    B *= i
    B %= p
for i in range(1, N - K + 1):  # calculate (N - K)!
    B *= i
    B %= p

B = square(B, (p - 2) % p)  # calculate B ** (p - 2) % p
print((A * B) % p)
