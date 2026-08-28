import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
left = 0
right = 0
is_visited = [False] * (max(L) + 1)
cnt = 0

while left <= N - 1:
    while right <= N - 1 and is_visited[L[right]] == False:
        is_visited[L[right]] = True
        right += 1
    cnt += right - left
    is_visited[L[left]] = False
    left += 1
    
print(cnt)