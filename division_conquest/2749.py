# 2749 / calculate fibonachi`s number with matrix
def fibo_mat(n):
    SIZE = 2  # fibonachi`s matrix size
    BASE, ZERO = [[1, 1], [1, 0]], [[1, 0], [0, 1]]  # BAZE is fibonachi result

    def matmul(a, b, size=SIZE):  # matrix multiple
        new = [[0] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    new[i][j] += (a[i][k] * b[k][j]) % 1000000
                    new[i][j] %= 1000000
        return new

    def loop(n=n):
        base, mat = BASE.copy(), ZERO.copy()
        k = 0
        while 2 ** k <= n:  # find 2 ** k under number n
            if n & (1 << k) != 0:
                mat = matmul(mat, base)  # multiple when 2 ** k
            k += 1
            base = matmul(base, base)  # multiple when others
        return mat

    return loop(n)[1][0]  # result


print(fibo_mat(int(input())))
