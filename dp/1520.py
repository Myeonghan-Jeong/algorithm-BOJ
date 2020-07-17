# 1520 / count pathes to reach end point with only go down
def dfs(i, j):
    global d, m, n, mat, dp

    # if reached end point, return 1 for calculate path
    if i == m - 1 and j == n - 1:
        return 1

    # if visited path, return path result
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 0
    for di, dj in d:
        ni, nj = i + di, j + dj
        # check next point is in map
        if 0 <= ni < m and 0 <= nj < n:
            # check next point is lower than now
            if mat[ni][nj] < mat[i][j]:
                # go down
                dp[i][j] += dfs(ni, nj)

    return dp[i][j]


d = ((0, 1), (1, 0), (0, -1), (-1, 0))
m, n = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
print(dfs(0, 0))
