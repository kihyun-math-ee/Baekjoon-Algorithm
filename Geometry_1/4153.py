import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    
    if a == 0 and b == 0 and c == 0:
        sys.exit(0)
    
    else:
        if (a ** 2) + (b ** 2) == (c ** 2):
            print('right')
        elif (b ** 2) + (c ** 2) == (a ** 2):
            print('right')
        elif (c ** 2) + (a ** 2) == (b ** 2):
            print('right')
        else:
            print('wrong')