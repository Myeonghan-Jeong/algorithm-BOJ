# 2869 / count days for snail to climb tree
import math

A, B, V = map(int, input().split())
print(math.ceil((V - B) / (A - B)))
