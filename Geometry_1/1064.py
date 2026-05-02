import sys
import math

x_a, y_a, x_b, y_b, x_c, y_c = map(int, sys.stdin.readline().split())
L = []

if (x_b - x_a) * (y_c - y_a) == (y_b - y_a) * (x_c - x_a):
    print(-1.0)

else:
    L.append(2*(math.sqrt((x_a-x_b)**2+(y_a-y_b)**2)+math.sqrt((x_c-x_a)**2+(y_c-y_a)**2)))
    L.append(2*(math.sqrt((x_a-x_b)**2+(y_a-y_b)**2)+math.sqrt((x_b-x_c)**2+(y_b-y_c)**2)))
    L.append(2*(math.sqrt((x_b-x_c)**2+(y_b-y_c)**2)+math.sqrt((x_c-x_a)**2+(y_c-y_a)**2)))
    print(max(L) - min(L))