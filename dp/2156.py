# 2156 / calculate max values without drink three consecutive wines
n = int(input())
wines = [0] + [int(input()) for _ in range(n)]

dp = [0, wines[1]]
if n > 1:
    dp.append(wines[1] + wines[2])

'''
cases without drink three consecutive wines
1: drink this wine and not drink previous wine
2: drink this wine and drink previous wine also
3: not drink this wine
'''

for i in range(3, n + 1):
    dp.append(max(wines[i] + dp[i - 2],
                  wines[i] + wines[i - 1] + dp[i - 3],
                  dp[i - 1]))

print(dp[n])
