import sys

A, B = map(int, sys.stdin.readline().split())
win_cnt = 0
deck = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
deck.remove(A)
deck.remove(B)

for i in range(18):
    for j in range(i + 1, 18):
        enemy_card1 = deck[i]
        enemy_card2 = deck[j]

        if A == B:
            if enemy_card1 == enemy_card2:
                if A > enemy_card1:
                    win_cnt += 1
            else:
                win_cnt += 1
        
        else:
            if enemy_card1 != enemy_card2:
                if (A + B) % 10 > (enemy_card1 + enemy_card2) % 10:
                    win_cnt += 1

print(f"{(win_cnt/153):.3f}")