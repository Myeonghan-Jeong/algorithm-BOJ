# 10872 / calculate n factorial
def fac(n):
    if n <= 1:  # 0! is 1
        return 1
    else:
        return fac(n - 1) * n


print(fac(int(input())))
