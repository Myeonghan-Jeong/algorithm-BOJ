# 1932 / calculate max sum start with top to end with one line
tree = [list(map(int, input().split())) for _ in range(int(input()))]
for i in range(1, len(tree)):
    for j in range(len(tree[i])):
        if j == 0:  # if first column
            tree[i][j] += tree[i - 1][j]
        elif j == len(tree[i]) - 1:  # if last column
            tree[i][-1] += tree[i - 1][-1]
        else:  # else check max previous number
            tree[i][j] += max(tree[i - 1][j - 1], tree[i - 1][j])
print(max(tree[-1]))
