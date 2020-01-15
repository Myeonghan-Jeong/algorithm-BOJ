# 1712 / find break-even point when sale in C
A, B, C = map(int, input().split())
res = int(A / (C - B)) + 1 if C > B else -1
print(res)
