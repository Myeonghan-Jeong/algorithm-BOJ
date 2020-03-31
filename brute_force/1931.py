# 1931 / calculate max meetings can do
N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
times.sort(key=lambda t: t[0])  # sort with start time
times.sort(key=lambda t: t[1])  # sort with end time

ended, cnt = 0, 0
for time in times:
    if ended <= time[0]:  # compare end time and start time
        ended = time[1]
        cnt += 1
print(cnt)
