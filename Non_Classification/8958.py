# 8958 / sum points of question with given rule
for T in range(int(input())):
    OXs = list(input())

    res, temp = 0, 0
    for i in range(len(OXs)):
        if OXs[i] == 'O':
            res += 1 + temp
            temp += 1
        else:
            temp = 0

    print(res)
