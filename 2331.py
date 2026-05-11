import sys

A, P = map(int, sys.stdin.readline().split())
target = []

while True:
    if A not in target:
        a = str(A)
        target.append(A)
        result = 0
        for i in range(len(a)):
            result += int(a[i])**P
        A = result
    
    else:
        idx = target.index(A)
        print(len(target[:idx]))
        sys.exit(0)
