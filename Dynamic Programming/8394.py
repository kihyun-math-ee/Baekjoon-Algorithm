import sys

n = int(sys.stdin.readline())

if n == 1:
    print(1)

elif n == 2:
    print(2)

else:
    an_2 = 1
    an_1 = 2
    an = 0

    for i in range(3, n + 1):
        an = (an_1 + an_2) % 10
        an_2 = an_1
        an_1 = an

    print(an)