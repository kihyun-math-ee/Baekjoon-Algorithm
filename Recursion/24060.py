import sys

save_cnt = 0
target_val = -1
K = 0

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global save_cnt, target_val, K
    i = p
    j = q + 1
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    
    while i <= q:
        tmp.append(A[i])
        i += 1

    while j <= r:
        tmp.append(A[j])
        j += 1
    i = p
    t = 0
    while i <= r:
        A[i] = tmp[t]
        save_cnt += 1
        if save_cnt == K:
            target_val = A[i]
        i += 1
        t += 1

N, K_input = map(int, sys.stdin.readline().split())
K = K_input
Sequence = list(map(int, sys.stdin.readline().split()))

merge_sort(Sequence, 0, len(Sequence) - 1)

if save_cnt < K:
    print(-1)
else:
    print(target_val)

