# 11066 / knuth`s optimization
for _ in range(int(input())):
    k = int(input())
    files = list(map(int, input().split()))

    dp = [[0 for _ in range(k)] for _ in range(k)]
    # cost for sum files from first to kth
    cost = [0] * (k + 1)
    cost[1] = files[0]
    for i in range(1, k + 1):
        cost[i] = cost[i - 1] + files[i - 1]

    # Knuth's Optimization
    knuth = [[0 for _ in range(k)] for _ in range(k)]
    for i in range(k):
        knuth[i][i] = i

    # summaried range
    for x in range(1, k):
        for i in range(k - x):
            j, dp[i][j] = i + x, float('inf')
            # apply knuth optimization
            for m in range(knuth[i][j - 1], knuth[i + 1][j] + 1):
                # calculate min
                if m < k - 1 and dp[i][j] > dp[i][m] + dp[m + 1][j] + cost[j + 1] - cost[i]:
                    dp[i][j] = dp[i][m] + dp[m + 1][j] + cost[j + 1] - cost[i]
                    knuth[i][j] = m

    print(dp[0][k - 1])
