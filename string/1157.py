# 1157 / find the most apperenced upper string
str_dict = {}
for s in input().upper():
    if s in str_dict:
        str_dict[s] += 1
    else:
        str_dict[s] = 1

check = []

maxV = max(str_dict.values())
for key, val in str_dict.items():
    if val == maxV:
        check.append(key)

if len(check) > 1:  # duplicated
    print('?')
else:
    print(check[0])
