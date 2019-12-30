# 1065 / find 'han number' has charcteristic in number
N = int(input())

cnt = 0
for i in range(1, N + 1):
    if i < 10:
        cnt += 1
    else:
        str_i = str(i)
        diff = int(str_i[0]) - int(str_i[1])
        for s in range(len(str_i) - 1):
            if int(str_i[s]) - int(str_i[s + 1]) != diff:
                break
        else:
            cnt += 1
print(cnt)
