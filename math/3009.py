# 3009 / find the last unknown point of reactangle
x, y = [], []
for _ in range(3):
    i, j = map(int, input().split())
    x.pop(x.index(i)) if i in x else x.append(i)
    y.pop(y.index(j)) if j in y else y.append(j)

print(x[0], y[0])
