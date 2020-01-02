# 10809 / find first idx number of each alphabets
string = input()
for char in 'abcdefghijklmnopqrstuvwxyz':
    for i in range(len(string)):
        if char == string[i]:
            print(i, end=' ')
            break
    else:
        print(-1, end=' ')
print()
