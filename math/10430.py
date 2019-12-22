# 10430 / check (A + B) % C is (A % C + B % C) % C and (A × B) % C is (A % C × B % C) % C
a, b, c = map(int, input().split())
print((a + b) % c)
print((a % c + b % c) % c)
print((a * b) % c)
print((a % c * b % c) % c)
