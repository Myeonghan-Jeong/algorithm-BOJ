# 14502 / calculate max safe area with 3 walls in lab
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


def bfs(lab, N, M):
    global res

    # start que
    f, r = -1, -1
    q = [0] * N * M * 2
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                r += 1
                q[r] = i
                r += 1
                q[r] = j
                visited[i][j] = 1

    # calculate max safe area
    while f != r:
        f += 1
        i = q[f]
        f += 1
        j = q[f]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if lab[ni][nj] == 0 and visited[ni][nj] == 0:
                    r += 1
                    q[r] = ni
                    r += 1
                    q[r] = nj
                    visited[ni][nj] = visited[i][j] + 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0 and visited[i][j] == 0:
                cnt += 1

    if res < cnt:
        res = cnt


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

res = 0
for i in range(N * M - 2):  # indexing points with modulus
    if lab[i // M][i % M] == 0:
        for j in range(i + 1, N * M - 1):
            if lab[j // M][j % M] == 0:
                for k in range(j + 1, N * M):
                    if lab[k // M][k % M] == 0:
                        lab[i // M][i % M] = 1
                        lab[j // M][j % M] = 1
                        lab[k // M][k % M] = 1
                        bfs(lab, N, M)
                        lab[i // M][i % M] = 0
                        lab[j // M][j % M] = 0
                        lab[k // M][k % M] = 0
print(res)
