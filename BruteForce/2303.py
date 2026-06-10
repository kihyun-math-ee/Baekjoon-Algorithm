import sys

N = int(sys.stdin.readline())
L = []

for x in range(N):
    M = 0
    target = list(map(int, sys.stdin.readline().split()))
    for i in range(3):
        for j in range(i + 1, 4):
            for k in range(j + 1, 5):
                if (target[i] + target[j] + target[k]) % 10 >= M:
                    M = (target[i] + target[j] + target[k]) % 10

    L.append((M, x + 1))

L.sort(reverse=True)
print(L[0][1])