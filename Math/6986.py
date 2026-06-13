import sys

N, K = map(int, sys.stdin.readline().split())
target = []

for _ in range(N):
    score = float(sys.stdin.readline())
    target.append(score)

target.sort()
revised_target = target[K:N-K]
T_mean = sum(revised_target) / (N-(2*K))

for i in range(0, K):
    target[i] = revised_target[0]
for j in range(N-K, N):
    target[j] = revised_target[-1]

A_mean = sum(target) / N

print(f"{T_mean + 1e-8:.2f}")
print(f"{A_mean + 1e-8:.2f}")