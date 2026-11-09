import sys

def permutation_cnt(n, l, num, s):
    global cnt
    global is_possible

    if is_possible:
        return
    
    if len(target) == n:
        cnt += 1
        if cnt == num:
            is_possible = True
            print(f"{s} {num} = {''.join(target)}")
        return    
        
    
    for i in range(n):
        if l[i] not in target:
            target.append(l[i])
            permutation_cnt(n, l, num, s)
            target.pop()

while True:
    line = sys.stdin.readline().split()
    if not line:
        break

    target = []
    cnt = 0
    is_possible = False
    S = line[0]
    N = int(line[1])
    L = []

    for j in range(len(S)):
        L.append(S[j])

    L.sort()

    permutation_cnt(len(L), L, N, S)
    if not is_possible:
        print(f"{S} {N} = No permutation")

    