# 17471 / calculate min diff of sum of areas
def linked(arr):  # check each area links
    global N, people, link

    q = [arr[0]]

    checked = [0] * (N + 1)
    checked[arr[0]] = 1

    submit = 0
    while q:
        r = q.pop(0)
        submit += people[r]

        for c in arr:
            if link[r][c] == 1 and checked[c] == 0:
                q.append(c)
                checked[c] = checked[r] + 1

    # if not linked all points in area
    for p in arr:
        if checked[p] == 0:
            return 0

    return submit


N = int(input())
people = [0] + list(map(int, input().split()))

link = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    puts = list(map(int, input().split()))

    for j in puts[1:]:
        link[i][j] = 1
        link[j][i] = 1

# set combinations with bit calculation
res = 100 * 100
for i in range(1, (1 << N) // 2):
    A, B = [], []

    for j in range(N):
        if i & (1 << j):
            A.append(j + 1)
        else:
            B.append(j + 1)

    rA = linked(A)
    rB = linked(B)
    if rA * rB != 0:
        diff = abs(rA - rB)
        if res > diff:
            res = diff

if res == 100 * 100:
    res = -1

print(res)
