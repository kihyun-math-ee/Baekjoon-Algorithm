import sys

N = int(sys.stdin.readline())
window_set = set()
j = 1

while True:
    i = 1

    while N >= i*j:

        if i*j not in window_set:
            window_set.add(i*j)

        else:
            window_set.remove(i*j)

        i += 1

    if j == N:
        break

    else:
        j += 1

print(len(window_set))