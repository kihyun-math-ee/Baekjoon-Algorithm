import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
L = [['X'] * (N + 2)]

for _ in range(N):
    S = sys.stdin.readline().strip()
    row = list(S)
    row = ['X'] + row + ['X']
    L.append(row)

L.append(['X'] * (N + 2))
is_visited_normal = [[False] * (N + 2) for _ in range(N + 2)]
is_visited_blind = [[False] * (N + 2) for _ in range(N + 2)]
cnt_normal = 0
cnt_blind = 0

def dfs_normal(normal_y, normal_x, color_normal):
    if is_visited_normal[normal_y + 1][normal_x] == False and L[normal_y + 1][normal_x] == color_normal:
        is_visited_normal[normal_y + 1][normal_x] = True
        dfs_normal(normal_y + 1, normal_x, color_normal)
    
    if is_visited_normal[normal_y][normal_x + 1] == False and L[normal_y][normal_x + 1] == color_normal:
        is_visited_normal[normal_y][normal_x + 1] = True
        dfs_normal(normal_y, normal_x + 1, color_normal)
    
    if is_visited_normal[normal_y - 1][normal_x] == False and L[normal_y - 1][normal_x] == color_normal:
        is_visited_normal[normal_y - 1][normal_x] = True
        dfs_normal(normal_y - 1, normal_x, color_normal)
    
    if is_visited_normal[normal_y][normal_x - 1] == False and L[normal_y][normal_x - 1] == color_normal:
        is_visited_normal[normal_y][normal_x - 1] = True
        dfs_normal(normal_y, normal_x - 1, color_normal)

    return
        
def dfs_blind(blind_y, blind_x, color_blind):
    if color_blind == 'R' or color_blind == 'G':
        
        if L[blind_y + 1][blind_x] == 'R' or L[blind_y + 1][blind_x] == 'G':
            if is_visited_blind[blind_y + 1][blind_x] == False:
                is_visited_blind[blind_y + 1][blind_x] = True
                dfs_blind(blind_y + 1, blind_x, color_blind)
        
        if L[blind_y][blind_x + 1] == 'R' or L[blind_y][blind_x + 1] == 'G':
            if is_visited_blind[blind_y][blind_x + 1] == False:
                is_visited_blind[blind_y][blind_x + 1] = True
                dfs_blind(blind_y, blind_x + 1, color_blind)
        
        if L[blind_y - 1][blind_x] == 'R' or L[blind_y - 1][blind_x] == 'G':
            if is_visited_blind[blind_y - 1][blind_x] == False:
                is_visited_blind[blind_y - 1][blind_x] = True
                dfs_blind(blind_y - 1, blind_x, color_blind)
        
        if L[blind_y][blind_x - 1] == 'R' or L[blind_y][blind_x - 1] == 'G':
            if is_visited_blind[blind_y][blind_x - 1] == False:
                is_visited_blind[blind_y][blind_x - 1] = True
                dfs_blind(blind_y, blind_x - 1, color_blind)

    elif color_blind == 'B':
        
        if L[blind_y + 1][blind_x] == 'B':
            if is_visited_blind[blind_y + 1][blind_x] == False:
                is_visited_blind[blind_y + 1][blind_x] = True
                dfs_blind(blind_y + 1, blind_x, color_blind)

        if L[blind_y][blind_x + 1] == 'B':
            if is_visited_blind[blind_y][blind_x + 1] == False:
                is_visited_blind[blind_y][blind_x + 1] = True
                dfs_blind(blind_y, blind_x + 1, color_blind)

        if L[blind_y - 1][blind_x] == 'B':
            if is_visited_blind[blind_y - 1][blind_x] == False:
                is_visited_blind[blind_y - 1][blind_x] = True
                dfs_blind(blind_y - 1, blind_x, color_blind)

        if L[blind_y][blind_x - 1] == 'B':
            if is_visited_blind[blind_y][blind_x - 1] == False:
                is_visited_blind[blind_y][blind_x - 1] = True
                dfs_blind(blind_y, blind_x - 1, color_blind)

    return
    
for y in range(1, N + 1):
    for x in range(1, N + 1):
        if is_visited_normal[y][x] == False and (L[y][x] == 'R' or L[y][x] == 'G' or L[y][x] == 'B'):
            is_visited_normal[y][x] = True
            dfs_normal(y, x, L[y][x])
            cnt_normal += 1
        if is_visited_blind[y][x] == False and (L[y][x] == 'R' or L[y][x] == 'G' or L[y][x] == 'B'):
            is_visited_blind[y][x] = True
            dfs_blind(y, x, L[y][x])
            cnt_blind += 1

print(cnt_normal, cnt_blind)