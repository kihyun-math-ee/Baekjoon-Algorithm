import sys

N = int(sys.stdin.readline())
original_board = []
cnt_1 = 0
cnt_2 = 0

for _ in range(N):
    line = sys.stdin.readline().strip()
    original_board.append(line)

for row in original_board:
    chunks = row.split('X')
    for chunk in chunks:
        if len(chunk) >= 2:
            cnt_1 += 1

col_list = []
for i in range(N):
    col_str = ''
    for j in range(N):
        col_str += original_board[j][i]
    col_list.append(col_str)

for col in col_list:
    chunks = col.split('X')
    for chunk in chunks:
        if len(chunk) >= 2:
            cnt_2 += 1

print(cnt_1, cnt_2)
