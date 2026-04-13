import sys

S = sys.stdin.readline().strip()
word_set = set()

for i in range(len(S)):
    word_set.add(S[i:])

print('\n'.join(sorted(word_set)))