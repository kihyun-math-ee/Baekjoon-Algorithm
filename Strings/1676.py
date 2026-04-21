import sys

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
N = int(sys.stdin.readline())
S = fact(N)
target = str(S)
i = 1
cnt = 0
check = 0

while True:
    if i > len(target):
        print(cnt)
        sys.exit(0)
    else:
        if int(target[-i]) == 0:
            cnt += 1
            i += 1
        else:
            print(cnt)
            sys.exit(0)