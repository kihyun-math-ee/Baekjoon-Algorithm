import sys

K = int(sys.stdin.readline())

for i in range(K):
    target = list(map(int, sys.stdin.readline().split()))
    student_num = target[0]
    score = target[1:]
    score = sorted(score, reverse=True)
    L_gap = 0

    for j in range(student_num - 1):
        if score[j] - score[j+1] >= L_gap:
            L_gap = score[j] - score[j+1]

    print(f'Class {i+1}')
    print(f'Max {score[0]}, Min {score[-1]}, Largest gap {L_gap}')