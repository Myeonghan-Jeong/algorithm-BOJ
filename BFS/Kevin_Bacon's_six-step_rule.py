# 1389(BFS, DFS) / calculate person who has the lowest Kevin Bacon number
N, M = map(int, input().split())

link = [[N + 1] * (N + 1) for _ in range(N + 1)]  # set link matrix
for m in range(M):
    a, b = map(int, input().split())
    link[a][b] = 1
    link[b][a] = 1

# Floyd-Warshall Algorithm #
for k in range(1, N + 1):
    for i in range(1, N + 1):
        if i != k:
            for j in range(1, N + 1):
                if j != i and j != k:
                    link[i][j] = min(link[i][k] + link[k][j], link[i][j])

cnt, people = N ** 2, N ** 2
for n in range(1, N + 1):
    temp = 0
    for c in range(1, N + 1):
        if n != c:
            temp += link[n][c]

    if cnt > temp:  # find the lowest Kevin-Bacon number
        cnt = temp
        people = n
    elif cnt == temp:  # find the lowest number who has same Kevin-Bacon number
        if people > n:
            people = n

print(people)
