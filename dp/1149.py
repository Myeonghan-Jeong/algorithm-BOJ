# 1149 / calculate min sum of cost for paint homes not continuous
homes = [list(map(int, input().split())) for _ in range(int(input()))]

dp = [[0] * 3 for _ in range(len(homes))]
for i in range(len(dp)):
    if i == 0:
        dp[i] = homes[i][:]
    else:
        # if paint this home red
        dp[i][0] = homes[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        # if paint this home green
        dp[i][1] = homes[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        # if paint this home blue
        dp[i][2] = homes[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[-1]))
