# 1541 / calculate min num with ()
# find - and sum all numbers back of -, than minus that into sum of all numbers front of -
plus, *minus = [sum(map(int, v.split('+'))) for v in input().split('-')]
print(plus - sum(minus))
