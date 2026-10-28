import sys

N, d, k, c = map(int, sys.stdin.readline().split())
L = []

for _ in range(N):
    sushi = int(sys.stdin.readline())
    L.append(sushi)

S = set(L)
num_list = [0] * (len(S))
target = L + L[:k]
check = dict(zip(S, num_list))
cases = 0
max_cases = 0

if check.get(c, 0) == 0:
    check[c] = 0

for j in range(k):
    if check[target[j]] == 0:
        cases += 1
    check[target[j]] += 1

current_score = cases

if check[c] == 0:
    current_score += 1

if max_cases < current_score:
    max_cases = current_score

for i in range(k, N + k):
    check[target[i - k]] -= 1

    if check[target[i - k]] == 0:
        cases -= 1

    if check[target[i]] == 0:
        cases += 1

    check[target[i]] += 1
    current_score = cases

    if check[c] == 0:
        current_score += 1

    if max_cases < current_score:
        max_cases = current_score

print(max_cases)