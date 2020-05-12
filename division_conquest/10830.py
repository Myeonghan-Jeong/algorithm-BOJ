# 10830 / calculate power of matrix
def power(p, n):
    global a

    if p == 1:
        return a
    elif p % 2 == 1:
        o, t = list(zip(*power(p - 1, n))), [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    t[i][j] += a[i][k] * o[j][k]
                    t[i][j] %= 1000
        return t
    else:
        l, t = power(p // 2, n), [[0] * n for _ in range(n)]
        r = list(zip(*l))
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    t[i][j] += l[i][k] * r[j][k]
                    t[i][j] %= 1000
        return t


n, b = map(int, input().split())
a = [[]] * n
for i in range(n):
    a[i] = list(map(int, input().split()))

r = power(b, n)
for i in range(n):
    for j in range(n):
        print(r[i][j] % 1000, end=' ')  # print rest of 1000
    print()
