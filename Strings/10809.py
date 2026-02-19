import sys
S = sys.stdin.readline().strip()

for x in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(x), end=' ')

