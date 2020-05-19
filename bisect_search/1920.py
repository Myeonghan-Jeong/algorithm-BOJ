# 1920 / find number in array
def find(n, s, e):
    global num

    if e - s == 1:
        return 1 if n in num[s:e + 1] else 0

    mid = (s + e) // 2
    if n == num[mid]:
        return 1
    elif n < num[mid]:
        return find(n, s, mid)
    elif n > num[mid]:
        return find(n, mid, e)


N = int(input())
num = list(map(int, input().split()))
num.sort()

M = int(input())
compares = list(map(int, input().split()))
for m in range(M):
    print(find(compares[m], 0, N - 1))
