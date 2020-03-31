# 11047 / calculate cnt of coins to make K(without DP)
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

cnt, idx = 0, N - 1
while K > 0:
    if K >= coins[idx]:
        K -= coins[idx]
        cnt += 1
    else:
        idx -= 1
print(cnt)
