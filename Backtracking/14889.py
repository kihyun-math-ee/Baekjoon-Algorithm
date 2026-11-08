import sys

N = int(sys.stdin.readline())
synergy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [False] * N
min_diff = float('inf')

def backtracking(idx, cnt):
    global min_diff

    if cnt == N // 2:
        total_start = 0
        total_link = 0

        for y in range(N):
            for x in range(N):

                if y != x:
                    if visited[y] and visited[x]:
                        total_start += synergy[y][x]
                    elif not visited[y] and not visited[x]:
                        total_link += synergy[y][x]

        if abs(total_start - total_link) < min_diff:
            min_diff = abs(total_start - total_link)

        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            backtracking(i + 1, cnt + 1)
            visited[i] = False

backtracking(0, 0)
print(min_diff)