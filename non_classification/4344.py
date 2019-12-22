# 4344 / calculate percent of number of over average
for C in range(int(input())):
    arr = list(map(int, input().split()))
    N, scores = arr[0], arr[1:]

    avg, res = sum(scores) / N, 0
    for score in scores:
        if score > avg:
            res += 1

    print('{:.3f}%'.format(round(res / N * 100, 3)))
