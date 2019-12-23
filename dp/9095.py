# 9095 / count number for make N with 1, 2, 3
dp = {1: 1, 2: 2, 3: 4}  # set DP dict


def find(n):
    global dp

    if n not in dp:
        temp = 0
        # minus i from N for find number for make N - i
        for i in [1, 2, 3]:
            if n - i >= 0:
                temp += find(n - i)
        dp[n] = temp

    return dp[n]


for T in range(int(input())):
    N = int(input())

    print(find(N))
