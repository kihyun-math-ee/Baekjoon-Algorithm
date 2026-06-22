import sys

N = int(sys.stdin.readline())
L = []
k = 1

for _ in range(N):
    line = sys.stdin.readline().strip()
    L.append(line)

while True:
    is_possible = True
    for i in range(0, N - 1):
        for j in range(i + 1, N):
            if L[i][-k:] == L[j][-k:]:
                is_possible = False
                break
        if is_possible == False:
            k += 1
            break
    if is_possible == True:
        print(k)
        break