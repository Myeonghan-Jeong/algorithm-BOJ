# 10039 / calculate avg of score with special rule
sco = 0
for _ in range(5):
    test = int(input())
    if test >= 40:  # if score is over 40
        sco += test  # add score
    else:
        sco += 40  # add 40
print(sco // 5)
