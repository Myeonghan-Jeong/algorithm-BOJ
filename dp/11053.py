# 11053 / sovle LIS problem with DP
from collections import deque

N = int(input())
arr = list(map(int, input().split()))

# solution 1: O(n ** 2)
'''
if there is arr = [10, 20, 10, 30, 50]
calculate LIS if the end number is arr[i]
'''
dp = [1] * N
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:  # check the ith number is higher than jth
            dp[i] = max(dp[i], dp[j] + 1)  # compare LIS
print(max(dp))

# solution 2: O(n * log(n))
dp = deque([-float('inf')])
for n in range(N):
    if dp[-1] < arr[n]:  # if number is bigger than the end
        dp.append(arr[n])  # append it
    else:
        for i in range(len(dp) - 1):  # find lower bound number in LIS
            if dp[i] < arr[n] <= dp[i + 1]:
                dp[i + 1] = arr[n]  # change it
                break
print(len(dp) - 1)
