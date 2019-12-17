# 17135 / count max number of killed enemy in castle defense
def ncr(n, r):  # batch 3 arrows with combination
    global combinations, c

    if not r:
        combinations.append(c[:])
    elif r > n:
        return
    else:
        c[r - 1] = n - 1
        ncr(n - 1, r - 1)
        ncr(n - 1, r)


def shoot(idx, n, m, d):  # shoot arrow in position
    global fake

    visited = [[0] * m for _ in range(n)]
    visited[n - 1][idx] = 1

    q = [[n - 1, idx]]
    while q:
        i, j = q.pop(0)
        if fake[i][j] >= 1:
            return [i, j]

        for si, sj in S:
            ni, nj = i + si, j + sj
            if 0 <= ni < n and 0 <= nj < m:
                ln = visited[i][j] + 1
                if ln <= d:
                    visited[ni][nj] = ln
                    q.append([ni, nj])


def defense(arr, n, m, d, s):  # defense castle
    global fake

    cnt = 0
    while s != 0:
        # kill enemy
        for p in arr:
            arrow = shoot(p, n, m, d)
            if arrow:
                i, j = arrow
                fake[i][j] += 1

        # count killed enemy
        for i in range(n):
            for j in range(m):
                if fake[i][j] > 1:
                    cnt += 1
                    s -= 1
                    fake[i][j] = 0

        # reset castle
        temp = 0
        for i in range(n - 1, -1, -1):
            if i == 0:
                fake[i] = [0] * m
            else:
                fake[i] = fake[i - 1][:]
                temp += sum(fake[i])

        s = temp

    return cnt


S = [[0, -1], [-1, 0], [0, 1]]  # search order

N, M, D = map(int, input().split())

summit = 0
castle = [[]] * N
for n in range(N):
    castle[n] = list(map(int, input().split()))
    summit += sum(castle[n])

combinations = []
c = [0] * 3
ncr(M, 3)

res = 0
for points in combinations:
    fake = [[]] * N
    for r in range(N):
        fake[r] = castle[r][:]

    dead = defense(points, N, M, D, summit)
    if res < dead:
        res = dead

print(res)
