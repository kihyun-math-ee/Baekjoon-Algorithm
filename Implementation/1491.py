import sys

N, M = map(int, sys.stdin.readline().split())
left = 0
right = N - 1
bottom = 0
top = M - 1

x = 0
y = 0

while True:
    if x < right:
        x = right
        bottom += 1
    else:
        break

    if y < top:
        y = top
        right -= 1
    else:
        break

    if x > left:
        x = left
        top -= 1
    else:
        break

    if y > bottom:
        y = bottom
        left += 1
    else:
        break

print(x, y)