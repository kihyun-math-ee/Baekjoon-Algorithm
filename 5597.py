import sys

submitted = []

for _ in range(28):
    n = int(sys.stdin.readline())
    submitted.append(n)

for i in range(1, 31):
    if i not in submitted:
        print(i)