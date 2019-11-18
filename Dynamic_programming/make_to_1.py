# 1463(Dynamic programming) / calculate min of number of using the lowest calculation
info = {1: 0, 2: 1}  # set basic dict


# set function with DP
def find(n):

    if n in info:  # check number is in dict
        return info[n]
    
    # find min number of calculation
    # n // k: number of divison calculation
    # n % k: number of minus calculation
    m = 1 + min(find(n // 2) + n % 2, find(n // 3) + n % 3)
    info[n] = m  # add result to dict

    return m


N = int(input())
print(find(N))


# 1463(with recursive)
def find(n, cnt):
    global res, arr

    # if number of calculation is over min res, return
    if cnt > res:
        return

    # if already calculated numeber, return
    if not arr[n]:
        return

    if n == 1:  # check final number is 1
        if res > cnt:  # renewal result
            res = cnt
    elif n <= 0:
        return

    if not n % 3:  # divide with 3
        arr[n] = 0
        find(n // 3, cnt + 1)
        arr[n] = 1
        
    if not n % 2:  # divide with 2
        arr[n] = 0
        find(n // 2, cnt + 1)
        arr[n] = 1
        
    arr[n] = 0  # minus calculation
    find(n - 1, cnt + 1)
    arr[n] = 1

    
N = int(input())

# set result and array with default value
res = 10 ** 6
arr = [0] + [1] * N
find(N, 0)
print(res)
