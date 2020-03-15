# 2475 / calculate validation number
codes = list(map(int, input().split()))
print(sum([code ** 2 for code in codes]) % 10)
