# 1330(undefined) / compare numbers and print result
a, b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')


# 1546(undefined) / calculate new average of array with special rule
N = int(input())
scores = list(map(int, input().split()))

top = max(scores)  # find max number in array
for i in range(N):
    scores[i] = round(scores[i] / top * 100, 2)

print(round(sum(scores) / len(scores), 2))
