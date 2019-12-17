# 1000 / calculate sum of numbers
print(sum(map(int, input().split())))


# 1001 / calculate diff of numbers
a, b = map(int, input().split())
print(a - b)


# 1008 / calculate divided result of numbers
a, b = map(int, input().split())
print(a / b)

# 10950 / calculate sum of numbers with loop
for i in range(int(input())):
    print(sum(map(int, input().split())))

# 10951 / calculate sum of numbers with EOF error
while True:
    try:
        print(sum(map(int, input().split())))
    except EOFError:
        break

# 10952 / calculate sum of numbers with checking ends
while True:
    res = sum(map(int, input().split()))
    if not res:
        break
    print(res)

# 10953 / calculate sum of numbers with split ,
for T in range(int(input())):
    print(sum(map(int, input().split(','))))

# 10998 / calculate multiple of numbers
a, b = map(int, input().split())
print(a * b)

# 11021 / calculate sum of numbers with case number
for i in range(int(input())):
    print(f'Case #{i + 1}: {sum(map(int, input().split()))}')

# 11022 / calculate sum of numbers with case number and equation
for i in range(int(input())):
    a, b = map(int, input().split())
    print(f'Case #{i + 1}: {a} + {b} = {a + b}')

# 15740 / calculate sum of numbers with big integer
print(sum(map(int, input().split())))
