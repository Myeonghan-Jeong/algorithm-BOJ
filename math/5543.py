# 5543 / calculate min sum of burger and coke
bugers = [int(input()) for _ in range(3)]
cokes = [int(input()) for _ in range(2)]
print(min(bugers) + min(cokes) - 50)
