# 1244(undefined) / calculate final state of switch
N = int(input())
switch = [2] + list(map(int, input().split()))  # original state of switch

M = int(input())
for i in range(M):
    g, n = map(int, input().split())  # g : gender, n : target number
    if g == 1:  # if gender is man
        j = n

        while j <= N:  # change state of switch which index number is multiple of n
            switch[j] = 1 - switch[j]
            j += n
    else:  # if gender is woman
        left, right = n, n

        while True:  # change state of switch if state of left and right switch is same
            if 0 < left and right <= N and switch[left] == switch[right]:
                switch[left], switch[right] = 1 - switch[left], 1 - switch[right]
            elif left <= 0 or right > N or switch[left] != switch[right]:
                break

            left -= 1
            right += 1  # move

res = ' '.join(map(str, switch[1:]))
while res:  # print joined result, cutting 40 letters
    print(res[:40])
    res = res[40:]
    