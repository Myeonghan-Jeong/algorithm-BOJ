# 2740 / calculate multiple of matrix
n, m = map(int, input().split())
a = [[]] * n
for i in range(n):
    a[i] = list(map(int, input().split()))

m, k = map(int, input().split())
b = [[]] * m
for i in range(m):
    b[i] = list(map(int, input().split()))
b = list(zip(*b))

s = [[0] * k for _ in range(n)]
for i in range(n):  # O(n ** 3)
    for j in range(k):
        ra, cb = a[i], b[j]
        for _ in range(m):
            s[i][j] += ra[_] * cb[_]
        print(s[i][j], end=' ')
    print()
