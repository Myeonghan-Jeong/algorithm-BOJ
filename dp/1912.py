# 1912 / calculate max continuous sum
n = int(input())
num = list(map(int, input().split()))

dp = [0] * n
res = -1001
# compare continuous sum and number
for i in range(n):
    dp[i] = max(dp[i - 1] + num[i], num[i])
    res = max(res, dp[i])
print(res)
