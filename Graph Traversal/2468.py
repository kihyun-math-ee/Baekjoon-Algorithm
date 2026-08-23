import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
L = [[0] * (N + 2)]
L_max = float('-inf')

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    if L_max < max(row):
        L_max = max(row)
    row = [0] + row + [0]
    L.append(row)

L.append([0] * (N + 2))
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
cnt_list = []

def dfs(Y, X):
    for i in range(4):
        if L[Y + dy[i]][X + dx[i]] > k and is_visited[Y + dy[i]][X + dx[i]] == False:
            is_visited[Y + dy[i]][X + dx[i]] = True
            dfs(Y + dy[i], X + dx[i])
    return

for k in range(L_max):
    is_visited = [[False] * (N + 2) for _ in range(N + 2)]
    range_cnt = 0
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            if L[y][x] > k and is_visited[y][x] == False:
                is_visited[y][x] = True
                dfs(y, x)
                range_cnt += 1
    cnt_list.append(range_cnt)

print(max(cnt_list))