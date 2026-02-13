import sys

paper = [[0] * 101 for _ in range(101)]
total_area = 0

N = int(sys.stdin.readline())

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if paper[i][j] == 0:
                paper[i][j] = 1
                total_area += 1

print(total_area)
