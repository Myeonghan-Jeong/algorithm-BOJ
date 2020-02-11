# 2798 / calculate max sum of picked 3 numbers under M
N, M = map(int, input().split())
cards = list(map(int, input().split()))

res = -1
for i in range(0, N):  # loop
    for j in range(i + 1, N):  # and loop
        for k in range(j + 1, N):  # and loop
            cal = cards[i] + cards[j] + cards[k]
            if cal <= M:
                res = max(res, cal)
print(res)
