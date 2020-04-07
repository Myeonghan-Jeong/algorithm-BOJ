# 1037 / calculate original number has given factors
N = int(input())
if N % 2 == 1:  # if number of real factor is odd
    print(sorted(map(int, input().split()))[N // 2] ** 2)
else:  # else
    factors = sorted(map(int, input().split()))
    print(factors[0] * factors[-1])
