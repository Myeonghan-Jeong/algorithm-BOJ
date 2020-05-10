# 1629 / calculate A ** B % C
def f(m, n, p):
    if n == 0:  # if power is 0
        return 1
    elif n == 1:  # if power is 1
        return m % p
    elif n % 2 == 1:  # if power is odd
        return ((m % p) * f(m, n - 1, p)) % p
    else:  # if power is even
        return f(m, n // 2, p) ** 2 % p


a, b, c = map(int, input().split())
print(f(a, b, c))
