# 2750 / sort numbers with O(n ** 2)
N = int(input())

nums = [0] * N
for _ in range(N):
    nums[_] = int(input())

nums.sort()
for _ in range(N):
    print(nums[_])


def insert_sort(arr):  # original solution: insert sort
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


nums = [int(input()) for _ in range(int(input()))]
print(insert_sort(nums))
