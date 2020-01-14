# 1316 / count group words
N = int(input())
words = [input() for _ in range(N)]

cnt = 0
for word in words:
    word_dict = {}
    for i in range(len(word)):
        if word[i] in word_dict:
            if abs(word_dict[word[i]] - i) == 1:  # if word is not group word
                word_dict[word[i]] = i
            else:
                break
        else:
            word_dict[word[i]] = i
    else:
        cnt += 1

print(cnt)
