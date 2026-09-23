import sys
import math

while True:
    target = list(map(float, sys.stdin.readline().split()))
    ans = []
    if len(target) == 1:
        if int(target[0]) == -1:
            break

    s_1 = math.sqrt(((target[0] - target[2]) ** 2) + ((target[1] - target[3]) ** 2))
    s_2 = math.sqrt(((target[2] - target[4]) ** 2 + (target[3] - target[5]) ** 2))
    s_3 = math.sqrt(((target[4] - target[0]) ** 2 + (target[5] - target[1]) ** 2))
    inner_product_1 = ((target[0] - target[2]) * (target[0] - target[4])) + ((target[1] - target[3]) * (target[1] - target[5]))
    inner_product_2 = ((target[2] - target[4]) * (target[2] - target[0])) + ((target[3] - target[5]) * (target[3] - target[1]))
    inner_product_3 = ((target[4] - target[0]) * (target[4] - target[2])) + ((target[5] - target[1]) * (target[5] - target[3]))

    def is_equal(a, b):
        return abs(a - b) < 0.01

    if s_1 >= s_2 + s_3 or s_2 >= s_3 + s_1 or s_3 >= s_1 + s_2:
        print('Not a Triangle')
    elif is_equal(s_1, s_2) and is_equal(s_2, s_3):
        ans.append('Equilateral')
    elif is_equal(s_1, s_2) or is_equal(s_2, s_3) or is_equal(s_3, s_1):
        ans.append('Isosceles')
    else:
        ans.append('Scalene')

    if ans:
        if inner_product_1 > 0 and inner_product_2 > 0 and inner_product_3 > 0:
            ans.append('Acute')
            print(*ans)
        elif inner_product_1 == 0 or inner_product_2 == 0 or inner_product_3 == 0:
            ans.append('Right')
            print(*ans)
        else:
            ans.append('Obtuse')
            print(*ans)
            