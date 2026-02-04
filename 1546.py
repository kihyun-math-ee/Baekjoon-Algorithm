import sys
N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
M = max(scores)

new_scores = []
for s in scores:
    new_scores.append(s / M * 100)
    
print(sum(new_scores) / N)