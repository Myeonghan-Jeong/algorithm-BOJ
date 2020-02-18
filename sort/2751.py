# 2751 / sort numbers with O(nlogn)
nums = [int(input()) for _ in range(int(input()))]
nums.sort()  # original sort in python has O(nlogn)
for num in nums:
    print(num)


def merge(left, right):  # original solution
    i, j = 0, 0
    arr = []
    # loop while one of the list ends up
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:  # compare numbers
            arr.append(left[i])  # add little number
            i += 1
        else:
            arr.append(right[j])
            j += 1

    # add left numbers in each list
    while i < len(left):
        arr.append(left[i])
        i += 1

    while j < len(right):
        arr.append(right[j])
        j += 1

    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left, right = arr[:mid], arr[mid:]
        l, r = merge_sort(left), merge_sort(right)  # devide 2 arr
        return merge(l, r)
    else:
        return arr


nums = [int(input()) for _ in range(int(input()))]
nums = merge_sort(nums)  # merge sort
for num in nums:
    print(num)
