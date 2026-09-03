import sys

N, K = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
S = set(L)
cnt = [0] * (len(S))
check = dict(zip(S, cnt))
left = 0
right = 0
max_length = 1

while right < N:
    if check[L[right]] < K:
        if max_length < right - left + 1:
            max_length = right - left + 1
        check[L[right]] += 1
        right += 1

    elif check[L[right]] >= K:
        check[L[left]] -= 1
        left += 1

print(max_length)