# 10871 / find numbers under X
num, x = map(int, input().split())
numbers = list(map(int, input().split()))
for number in numbers:
    if number < x:
        print(number)
