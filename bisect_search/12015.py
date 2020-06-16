# 12015 / calculate len of the longest LIS
from collections import deque
import sys


def lis(n, arr):
    dp = deque([0])

    for i in range(n):
        s, e = 0, len(dp) - 1

        while s <= e:
            mid = (s + e) // 2
            # if mid number of dp is lower than now number
            if dp[mid] < arr[i]:
                # up lower bound
                s = mid + 1
            else:
                # down upper bound
                e = mid - 1

        # if lower bound is larger than len of dp, this number is final number of LIS which len is index
        if s >= len(dp):
            dp.append(arr[i])
        # else, this number is the lowest number of LIS which len is index
        else:
            dp[s] = arr[i]

    return len(dp) - 1


N = int(input())
num = list(map(int, sys.stdin.readline().strip().split()))
print(lis(N, num))
