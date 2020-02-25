# 1181 / sort words with len and dictionary
words = list(set(input() for _ in range(int(input()))))
words.sort(key=lambda word: (len(word), word))
for word in words:
    print(word)
