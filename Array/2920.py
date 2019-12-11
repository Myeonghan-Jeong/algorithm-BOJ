# 2920 / check scale is ascending or not
piano = list(map(int, input().split()))

res = 'ascending'
for i in range(7):
    if piano[i] - piano[i + 1] == -1:
        if res != 'ascending':
            res = 'mixed'
            break
    elif piano[i] - piano[i + 1] == 1:
        if i == 0:
            res = 'descending'
        if res != 'descending':
            res = 'mixed'
            break
    else:
        res = 'mixed'
        break

print(res)
