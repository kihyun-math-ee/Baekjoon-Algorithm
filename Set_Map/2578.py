import sys

target = {}
row_hits = [0, 0, 0, 0, 0]
col_hits = [0, 0, 0, 0, 0]
diog1_hit = 0
diog2_hit = 0
cnt = 0
idx = 0

for i in range(5):
    Q = list(map(int, sys.stdin.readline().split()))
    for j in range(5):
        target[Q[j]] = (i, j)

for k in range(5):
    A = list(map(int, sys.stdin.readline().split()))
    for num in A:
        idx += 1
        r, c = target[num]
        row_hits[r] += 1
        col_hits[c] += 1
        
        if row_hits[r] == 5:
            cnt += 1
        if col_hits[c] == 5:
            cnt += 1

        if r == c:
            diog1_hit += 1
            if diog1_hit == 5:
                cnt += 1
        
        if r == 4 - c:
            diog2_hit += 1
            if diog2_hit == 5:
                cnt += 1

        if cnt >= 3:
            print(idx)
            sys.exit(0)




