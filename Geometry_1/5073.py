import sys

while True:
    
    a, b, c = map(int, sys.stdin.readline().split())
    
    if a == b == c == 0:
        break

    elif a == b == c:
        print("Equilateral")
    
    elif (a == b or b == c or c == a) and (a + b > c and b + c > a and c + a > b):
        print("Isosceles")

    elif (a + b > c and b + c > a and c + a > b):
        print("Scalene")

    else:

        print("Invalid")
