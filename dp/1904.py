# 1904 / calculate number of tiles which length is N
dp = [0] * (int(input()) + 1)
dp[1], dp[2] = 1, 2
for i in range(3, len(dp)):
    dp[i] = (dp[i - 1] % 15746 + dp[i - 2] % 15746) % 15746
print(dp[-1])
