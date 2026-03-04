import sys

N = int(sys.stdin.readline())
my_cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
target_cards = list(map(int, sys.stdin.readline().split()))
cnt_cards = {}

for x in my_cards:
    if x in cnt_cards:
        cnt_cards[x] += 1
    else:
        cnt_cards[x] = 1

answer = []
for y in target_cards:
    answer.append(cnt_cards.get(y, 0))

print(*answer)



