import sys
S = sys.stdin.readline().strip()
alphabet = [-1] * 26

for i, char in enumerate(S):
    idx = ord(char) - ord('a')
    if alphabet[idx] == -1:
        alphabet[idx] = i

print(*alphabet)
