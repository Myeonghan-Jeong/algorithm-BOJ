# 9251 / find LCS
W1, W2 = input(), input()  # input each words

'''
LCS: find longest common sequence between 2 sentences

matrix col: standard sentence, row: compared sentence
check char of standard and compared is same
if it is, LCS add 1 length
else, LCS is max LCS of each 2 partial sentence

ex:
W1, W2 = ABCD, ABEB
  0 A B E B
0 0 0 0 0 0
A 0 1 1 1 1: compare A:A, AB, ABE, ABEB
B 0 1 2 2 2: compare AB:A, AB, ABE, ABEB
C 0 1 2 2 2
D 0 1 2 2 2
'''

mat = [[0] * (len(W1) + 1) for _ in range(len(W2) + 1)]  # word mat
for i in range(1, len(W2) + 1):
    for j in range(1, len(W1) + 1):
        if W1[j - 1] == W2[i - 1]:  # if same char
            mat[i][j] = mat[i - 1][j - 1] + 1  # plus 1 to previous LCS
        else:
            mat[i][j] = max(mat[i - 1][j], mat[i][j - 1])  # return max LCS
print(max(mat[-1]))
