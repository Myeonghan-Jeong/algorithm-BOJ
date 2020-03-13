# 2579 / calculate max sum of score in stairs
from collections import deque

n = int(input())
stairs = [int(input()) for _ in range(n)]

if n == 0:  # if there is no stair
    print(0)
elif n == 1:  # if there is only one stair
    print(stairs[0])
elif n == 2:  # if there are two stairs
    print(sum(stairs))
else:  # if there are more than three stairs
    dp = deque()
    dp.append(stairs[0])
    dp.append(dp[0] + stairs[1])
    dp.append(max(dp[0] + stairs[2], stairs[1] + stairs[2]))

    for i in range(3, n):
        # equation: max score of n is n plus max of n - 1 + n - 3 and n - 2
        dp.append(stairs[i] + max(stairs[i - 1] + dp[i - 3], dp[i - 2]))

    print(dp[-1])
