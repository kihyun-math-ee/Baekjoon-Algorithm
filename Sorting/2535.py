import sys

player_status = []
award = []
N = int(sys.stdin.readline())

for _ in range(N):
    country, num, score = map(int, sys.stdin.readline().split())
    player_status.append((score, country, num))

player_status.sort(reverse=True)

award.append(player_status[0])
award.append(player_status[1])

for i in range(2, len(player_status)):
    if award[0][1] == award[1][1] and award[0][1] == player_status[i][1]:
        continue

    award.append(player_status[i])
    break

for j in range(3):
    print(award[j][1], award[j][2])

