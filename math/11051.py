# 11051 / calculate nCk with dp
N, K = map(int, input().split())
mat = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    for j in range(N + 1):
        if j > i:
            break
        elif j == 0:
            mat[i][j] = 1
        elif i == j:
            mat[i][j] = 1
        elif 0 < j < i:
            mat[i][j] = (
                mat[i - 1][j - 1] % 10007 + mat[i - 1][j] % 10007
            ) % 10007
print(mat[N][K])
