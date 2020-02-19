# 10989 / sort numbers with counting sort
import sys

N = int(input())
res = [0 for _ in range(10001)]  # max number is under 10000
for num in sys.stdin:
    res[int(num)] += 1  # count

for i in range(10001):  # print
    if res[i] > 0:
        for j in range(res[i]):
            print(i)


def counting_sort(arr, n):  # original solution: counting sort
    res, cnt = [-1] * n, [0] * (n + 1)
    for a in arr:  # count
        cnt[a] += 1

    for i in range(n - 1):  # update count arr
        cnt[i + 1] += cnt[i]

    for i in reversed(range(n)):  # sort items
        res[cnt[arr[i]] - 1] = arr[i]
        cnt[arr[i]] -= 1

    return res


nums = [int(input()) for _ in range(int(input()))]
nums = counting_sort(nums, len(nums))
for n in nums:
    print(n)
