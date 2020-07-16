# 11049 / calculate min multiple count for multiple matrix
n, mat = int(input()), []
for _ in range(n):
    mat.append(list(map(int, input().split())))

'''
IDEA:
  A B C D
A 0 1 3 8
B 0 0 2 5 -> if diff is more than 2, calculte like below equation
C 0 0 0 3 -> if diff is 1, just calculate
D 0 0 0 0 -> reverse and self calculation is not allowed for matrix

min calulate count of two maxtix:
min(ABCD) = min(
    ABCD,
    min(A) + min(BCD) + cost(row A * col A * col D),
    min(AB) + min(CD) + cost(row A * col B * col D),
    min(ABC) + min(D) + cost(row A * col C * col D),
)
'''

dp = [[0] * n for _ in range(n)]
# number of diagonal line
for i in range(1, n):
    # number of index for calculate
    for j in range(n - i):
        # if diff is 1, just multiple
        if i == 1:
            dp[j][j + 1] = mat[j][0] * mat[j][1] * mat[j + 1][1]
            continue
        # set max value
        dp[j][j + i] = 2 ** 32
        # calculate matrix with solution ides
        for k in range(j, j + i):
            dp[j][j + i] = min(dp[j][j + i],
                               dp[j][k] + dp[k + 1][j + i] + mat[j][0] * mat[k][1] * mat[j + i][1])
print(dp[0][n - 1])
