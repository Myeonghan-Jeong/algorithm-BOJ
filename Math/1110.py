# 1110 / calculate loop to make original number with a rule
N = input()

org = N  # save original number
if len(N) == 1:  # if len is 1, add 0 in front of number
    org = '0' + org

cycle = 0
while True:  # change number with a rule
    if len(N) == 1:
        N = '0' + N

    temp = 0
    for n in N:
        temp += int(n)

    temp = str(temp)[-1]
    N = N[1] + temp

    cycle += 1
    if N == org:
        print(cycle)
        break
