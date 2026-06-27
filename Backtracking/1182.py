import sys

target = []
cnt = 0
def subsequence(start, x, n, m):
    global cnt

    for i in range(start, n):
        target.append(x[i])
        if sum(target) == m:
            cnt += 1
        subsequence(i + 1, x, n, m)
        target.pop()

N, M = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
subsequence(0, L, N, M)
print(cnt)