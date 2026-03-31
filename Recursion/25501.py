import sys

def recursion(s, l, r, cnt):
    if l >= r:
        print(1, cnt)
    elif s[l] != s[r]:
        print(0, cnt)
    else:
        return recursion(s, l + 1, r - 1, cnt + 1)
    
def isPalindrom(s):
    return recursion(s, 0, len(s) - 1, 1)

T = int(sys.stdin.readline())
for _ in range(T):
    S = sys.stdin.readline().strip()
    isPalindrom(S)
