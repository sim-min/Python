word = input()

word_reverse = list(word)
word_origin = list(word_reverse)
word_reverse.reverse()

if word_reverse == word_origin:
    print(1)
else:
    print(0)