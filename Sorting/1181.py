import sys

N = int(sys.stdin.readline())
unique_words = set()
word_list = []

for _ in range(N):
    word = sys.stdin.readline().strip()
    unique_words.add(word)

for word in unique_words:
    word_list.append([len(word), word])

word_list.sort()

for i in range(len(word_list)):
    print(word_list[i][1])