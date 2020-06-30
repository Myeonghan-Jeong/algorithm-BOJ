# 2293 / count number of cases to make k with n coins
import sys

read = sys.stdin.readline
n, k = map(int, read().strip().split())
coins = [int(read().strip()) for _ in range(n)]

# value of dp means number of cases to make index with some coins
dp = [0 for _ in range(k + 1)]
# there is always one case to make k with only use one class of coin
dp[0] = 1
for i in coins:
    # loop from coin to k
    for j in range(i, k + 1):
        # if j is bigger than value of coin, plus cases of diff index
        if j - i >= 0:
            dp[j] += dp[j - i]
print(dp[k])
