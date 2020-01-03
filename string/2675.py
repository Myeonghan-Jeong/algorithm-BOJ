# 2675 / repeat alphabets R times
for T in range(int(input())):
    R, P = input().split()
    for p in P:
        print(p * int(R), end='')
    print()
