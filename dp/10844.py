# 10844 / find all stair numbers(diff of number of nth and n - 1th is 1)
N = int(input())

dp = [[0 for i in range(10)] for j in range(N + 1)]
for j in range(1, 10):
    dp[1][j] = 1

'''
if the end number is 0 ~ 9, there is special rule

num 0 1 2 3 4 5 6 7 8 9
1st 0 1 1 1 1 1 1 1 1 1
2nd 1 1 2 2 2 2 2 2 2 1
3th 1 3 3 4 4 4 4 4 3 2

number of ends with 0 ~ 9 is sum of previous digit number ends with n - 1, n + 1
'''

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:  # if num ends 0
            dp[i][j] = dp[i - 1][1]
        elif j == 9:  # if num ends 9
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[N]) % 1000000000)
