# 2562 / find max number and idx of it
idx, res = 0, 0
for i in range(9):
    N = int(input())
    if res < N:
        res, idx = N, i + 1

print(res)
print(idx)
