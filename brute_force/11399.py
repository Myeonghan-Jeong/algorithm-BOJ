# 11399 / calculate min time for spend in ATM
N = int(input())
P = sorted(list(map(int, input().split())))  # sort ASC

time = 0
for p in range(1, N + 1):
    time += sum(P[:p])
print(time)
