# 1110(math) / calculate number of loop to make original number with special rule
N = input()

original = N  # save original number
if len(N) == 1:  # if len of start number is 1, add 0 in front of number
    original = '0' + original

cycle = 0
while True:  # change number with given rule of problem
    if len(N) == 1:
        N = '0' + N

    temp = 0
    for n in N:
        temp += int(n)

    temp = str(temp)
    if len(temp) == 1:
        N = N[1] + temp
    else:
        N = N[1] + temp[1]

    cycle += 1

    if N == original:
        print(cycle)
        break
