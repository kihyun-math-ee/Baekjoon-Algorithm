import sys

target = []
global M
M = 0

def backtrack(n, k, current_num, s):
    global M

    if current_num > n:
        return
    
    M = max(M, current_num)

    for i in range(k):
        backtrack(n, k, current_num * 10 + s[i], s)
        
N, K = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))
sequence.sort()
backtrack(N, K, 0, sequence)

print(M)