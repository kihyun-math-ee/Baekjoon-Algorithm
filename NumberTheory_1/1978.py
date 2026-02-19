import sys
N = int(sys.stdin.readline())
line = sys.stdin.readline().split()
cnt = N

for i in range(len(line)):
    num = int(line[i])
    if num == 1:
            cnt -= 1
            continue
    for j in range(2, num):
        if int(line[i]) % j == 0:
            cnt -= 1
            break
    
print(cnt)