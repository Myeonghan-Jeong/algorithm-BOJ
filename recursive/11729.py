# 11729 / play hanoi tower
def hanoi(disk, start, mid, end):
    if disk == 1:
        print(start, end)  # if left disk is 1, move 1 to 3
    else:
        hanoi(disk - 1, start, end, mid)  # move n - 1 disks 1 to 2
        print(start, end)
        hanoi(disk - 1, mid, start, end)  # move n - 1 disks 2 to 3


N = int(input())

cnt = 0
for i in range(N):
    cnt += 2 ** i

print(cnt)
hanoi(N, 1, 2, 3)
