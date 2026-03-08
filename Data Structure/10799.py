import sys

S = sys.stdin.readline().strip()
domain = len(S)
stick_start = []
stick_end = []
laser_coordinate = []

for i in range(0, domain - 1):
    
    if S[i] == '(':
        if S[i + 1] == ')':
            laser_coordinate.append(((2*i) + 1) / 2)

        else:
            stick_start.append(i)

    if S[i] == ')':
        if S[i + 1] == ')':
            stick_end.append(i + 1)

total_stick = len(stick_start)

for x in laser_coordinate:
    for j in range(len(stick_start)):
        if stick_start[j] < x < stick_end[j]:
            total_stick += 1

print(total_stick)
