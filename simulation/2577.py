# 2577 / calculate multiple of numbers and count amount of each number
numbers = [0] * 10

val = 1
for i in range(3):
    val *= int(input())

val = str(val)
for v in val:
    numbers[int(v)] += 1

for i in range(10):
    print(numbers[i])
