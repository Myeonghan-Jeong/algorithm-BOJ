# 1874 / check sequence is right
s, cmd = [], []
cnt, pos = 1, True
for i in range(int(input())):
    num = int(input())
    while cnt <= num:  # find cnt same as num
        s.append(cnt)  # append cnt in s
        cmd.append('+')  # append + in cmd
        cnt += 1
    if s[-1] == num:  # if num is in the last of s
        s.pop()
        cmd.append('-')  # append - in cmd
    else:  # or break making cmd
        pos = False
        break

if not pos:
    print('NO')
else:
    for c in cmd:
        print(c)
