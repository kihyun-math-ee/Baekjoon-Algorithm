import sys

dials = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = sys.stdin.readline().strip()

total_time = 0
for char in word:
    for i, group in enumerate(dials):
        if char in group:
            total_time += (i + 3)
            break
print(total_time)