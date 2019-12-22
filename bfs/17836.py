# 17836 / find route takes min moving
def find():
    global N, M, T, castle

    # start que
    f, r = -1, -1
    q = [[0, 0] for _ in range(N * M)]

    # find route
    r += 1
    road, sword = N ** 3 * M ** 3, N ** 3 * M ** 3
    while f != r:
        f += 1
        i, j = q[f]

        if castle[i][j] == 2:
            sword = checked[i][j] + abs(N - 1 - i) + abs(M - 1 - j) - 1

        if i == N - 1 and j == M - 1:
            road = checked[i][j] - 1

        for di, dj in D:
            ni, nj = i + di, j + dj

            if 0 <= ni < N and 0 <= nj < M:
                if castle[ni][nj] != 1:
                    if checked[ni][nj] == 0:
                        checked[ni][nj] = checked[i][j] + 1
                        r += 1
                        q[r] = [ni, nj]

    # compare min route
    res = min(road, sword)
    if res <= T:
        return res

    return 'Fail'


D = [[0, 1], [1, 0], [0, -1], [-1, 0]]

N, M, T = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]
checked = [[0] * M for _ in range(N)]

checked[0][0] = 1
print(find())
