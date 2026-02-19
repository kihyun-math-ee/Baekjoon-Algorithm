import sys
N = int(sys.stdin.readline())
cnt = 0

for _ in range(N):
    word = sys.stdin.readline().strip()
    indices = [word.find(x) for x in word]
    if indices == sorted(indices):
        cnt += 1
        
print(cnt)