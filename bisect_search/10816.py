# 10816 / count target number cards
n = int(input())
cards = list(map(int, input().split()))

cnt = {}
for c in cards:
    cnt[c] = 1 if c not in cnt else cnt[c] + 1

m = int(input())
num = list(map(int, input().split()))
for i in range(m):
    print(cnt.get(num[i], 0), end=' ')
