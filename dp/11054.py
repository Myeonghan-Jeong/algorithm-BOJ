# 11054 / find LBS(appended question of 11053)
N = int(input())
arr = list(map(int, input().split()))

# dp[0], dp[1]: LIS(increasing), LDS(decreasing)
dp = [[1, 1] for _ in range(N)]
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            # when increasing compare LIS
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        elif arr[i] < arr[j]:
            # when decreasing compare just LDS and LIS + LDS(LBS)
            dp[i][1] = max(dp[i][1], dp[j][0] + 1, dp[j][1] + 1)

res = 0
for p in dp:
    res = max(res, p[0], p[1])
print(res)
