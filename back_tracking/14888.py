# 14888 / put operators in numbers and calculate min and max
def make_equation(idx, arr, res):
    global nums, minV, maxV

    if sum(arr) == 0:  # if put all operators
        if minV > res:
            minV = res
        if maxV < res:
            maxV = res
    else:
        if arr[0] != 0:  # plus
            arr[0] -= 1
            make_equation(idx + 1, arr, res + nums[idx + 1])
            arr[0] += 1
        if arr[1] != 0:  # minus
            arr[1] -= 1
            make_equation(idx + 1, arr, res - nums[idx + 1])
            arr[1] += 1
        if arr[2] != 0:  # mul
            arr[2] -= 1
            make_equation(idx + 1, arr, res * nums[idx + 1])
            arr[2] += 1
        if arr[3] != 0:  # devide
            arr[3] -= 1
            if res < 0:  # calculate devide as C++14 rule
                res = -(-res // nums[idx + 1])
            else:
                res = res // nums[idx + 1]
            make_equation(idx + 1, arr, res)
            arr[3] += 1


N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

minV, maxV = float('inf'), float('-inf')
make_equation(0, ops, nums[0])
for num in [maxV, minV]:
    print(num)
