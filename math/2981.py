# 2981 / find factors with same left in numbers
def gcd(a, b):
    while True:
        if a % b > 0:
            a, b = b, a % b
        else:
            return b


def factor(x):
    factors = [x]
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:  # mod
            factors.append(i)
            if x // i != i:  # factor
                factors.append(x // i)
    factors.sort()
    return factors


N = int(input())
nums = sorted([int(input()) for _ in range(N)], reverse=True)

diffs = [nums[i] - nums[i + 1] for i in range(len(nums) - 1)]
if len(diffs) == 1:
    ans = diffs[0]
elif len(diffs) == 2:
    ans = gcd(*diffs)
else:
    ans = diffs[0]
    for i in range(1, len(diffs)):
        ans = gcd(ans, diffs[i])

for n in factor(ans):
    print(n, end=' ')
