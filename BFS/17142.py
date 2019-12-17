# 17142 / find min time for spread all viruses
def ncr(n, r):  # select starting viruses
    global combinations, c

    if not r:
        combinations.append(c[:])
    elif r > n:
        return
    else:
        c[r - 1] = n - 1
        ncr(n - 1, r - 1)
        ncr(n - 1, r)


def spread(arr, s, n, t):
    global viruses, lab

    visited = [[-1] * n for _ in range(n)]

    # start que
    q = []
    for p in arr:
        [pi, pj] = viruses[p]
        q.append([pi, pj])
        visited[pi][pj] = 0

    # start spread target viruses
    while q:
        i, j = q.pop(0)
        s -= 1

        for di, dj in D:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if visited[ni][nj] == -1:
                    if lab[ni][nj] != 1:
                        visited[ni][nj] = visited[i][j] + 1
                        q.append([ni, nj])

    # check untargeted viruses and set there time 0
    unchecked = []
    for p in range(t):
        if p not in arr:
            unchecked.append(viruses[p])

    for un in unchecked:
        i, j = un
        visited[i][j] = 0

    # calculate min time for spread
    if s == 0:
        fin = 0
        for i in range(n):
            for j in range(n):
                if fin < visited[i][j]:
                    fin = visited[i][j]
        return fin
    return float('inf')


D = [[0, 1], [1, 0], [0, -1], [-1, 0]]
N, M = map(int, input().split())

cnt = 0
viruses, lab = [], [[]] * N
for n in range(N):
    lab[n] = list(map(int, input().split()))
    for m in range(N):
        if lab[n][m] == 2:
            viruses.append([n, m])
            cnt += 1
        elif lab[n][m] == 0:
            cnt += 1

T = len(viruses)
combinations = []
c = [0] * M
ncr(T, M)

res = float('inf')
for targets in combinations:
    time = spread(targets, cnt, N, T)
    if res > time:
        res = time

if res == float('inf'):
    res = -1

print(res)
