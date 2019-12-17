# 15552 / calculate sum of numbers with sys.readline
import sys

for i in range(int(input())):
    print(sum(map(int, sys.stdin.readline().rstrip().split())))
