# 2565 / count cutted lines for not tangled lines
N = int(input())
lines = sorted([list(map(int, input().split())) for _ in range(N)])

dp = [0] * N
dp[0] = 1

# find LIS with each lines
for i in range(1, N):
    links = 0
    for j in range(i):
        # compare lengthn of LIS
        if lines[i][1] > lines[j][1]:
            links = max(dp[j], links)
    dp[i] = links + 1  # add 1 for link itself
print(N - max(dp))  # cutted lines
