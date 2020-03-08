# 1003 / calculate called number of fibo(0) and fibo(1)
nums = {0: [1, 0], 1: [0, 1]}


def fibo(n):

    if n not in nums:
        n1, n2 = fibo(n - 1), fibo(n - 2)
        nums[n] = [n1[0] + n2[0], n1[1] + n2[1]]

    return nums[n]


for _ in range(int(input())):
    res = fibo(int(input()))
    print(res[0], res[1])
