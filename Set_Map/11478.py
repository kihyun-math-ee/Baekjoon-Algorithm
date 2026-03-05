import sys

S = sys.stdin.readline().strip()
sequential_S_set = set()

for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        sequential_S_set.add(S[i:j])

print(len(sequential_S_set))
    
