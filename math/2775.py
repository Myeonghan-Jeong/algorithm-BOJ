# 2775 / calculate people lives in floor k, room n
mat = [[0] * 15 for _ in range(15)]  # set apartment
for i in range(15):
    for j in range(15):
        if i == 0:
            mat[i][j] = j + 1
        else:
            mat[i][j] = sum(mat[i - 1][:j + 1])

for _ in range(int(input())):
    k, n = int(input()), int(input())
    print(mat[k][n - 1])
