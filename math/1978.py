# 1978 / find prime numbers under 1000
seele = [0] * 1001
seele[0], seele[1] = 1, 1
for i in range(2, 1001):  # find prime numbers under 1000
    num = 2 * i  # check non-prime numbers
    while num <= 1000:
        seele[num] = 1
        num += i

N = int(input())
numbers = list(map(int, input().split()))

sco = 0
for number in numbers:
    if seele[number] == 0:  # check prime number
        sco += 1

print(sco)
