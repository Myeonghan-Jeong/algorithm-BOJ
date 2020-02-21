# 1427 / sort numbered string with DESC
N = list(map(int, list(input())))
N.sort(reverse=True)
print(''.join(map(str, N)))
