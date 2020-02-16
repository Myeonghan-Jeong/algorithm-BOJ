# 1436 / find nth devil number
N = int(input())

num = 0
while N > 0:
    num += 1
    if '666' in str(num):  # if 666 in num, that is devil number
        N -= 1
print(num)
