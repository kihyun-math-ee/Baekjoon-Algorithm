import sys
word = sys.stdin.readline().strip()
print(int(word == word[::-1]))