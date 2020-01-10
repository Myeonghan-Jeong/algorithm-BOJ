# 2941 / count alphabets with croatia alphabets
croatia = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

i, cnt = 0, 0
while i < len(word):
    if word[i:i + 2] in croatia:
        cnt += 1
        i += 2
    elif word[i:i + 3] == 'dz=':
        cnt += 1
        i += 3
    else:
        cnt += 1
        i += 1

print(cnt)
