# 1992 / zip matrix with quad tree
def quad(si, sj, ei, ej, n):  # si, sj: start, ei, ej: end, n: len of partial mat
    global mat

    if n == 1:  # if len of sqaure is 1, return color
        return mat[si][sj]

    mid = n // 2  # divide mat
    r1 = quad(si, sj, si + mid, sj + mid, mid)  # 4th quadrant
    r2 = quad(si, sj + mid, si + mid, ej, mid)  # 1st quadrant
    r3 = quad(si + mid, sj, ei, sj + mid, mid)  # 3rd quadrant
    r4 = quad(si + mid, sj + mid, ei, ej, mid)  # 2nd quadrant

    if r1 == r2 == r3 == r4 and len(r1) == 1:  # if sqaure has only one color
        return r1
    return '(' + r1 + r2 + r3 + r4 + ')'  # sqaure has two colors


N = int(input())
mat = [list(input()) for _ in range(N)]  # original matrix
print(quad(0, 0, 0, 0, N))
