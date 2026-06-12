import sys

while True:
    n, k = map(int, sys.stdin.readline().split())
    if n == -1 and k == -1:
        break

    coefficients = list(map(int, sys.stdin.readline().split()))
    
    if k == 0:
        print(0)
    else:
        if n >= k:
            remainder_list = []
            for i in range(k):
                a = i // k
                remainder_list.append(((-1) ** (a) * coefficients[i]))
            for j in range(k, len(coefficients)):
                a = j // k
                b = j % k
                remainder_list[b] += ((-1) ** a) * coefficients[j]
            if remainder_list.count(0) == k:
                print(0)
            else:
                while True:
                    if remainder_list[-1] == 0:
                        remainder_list.pop()
                    else:
                        break
                print(*remainder_list)

        else:
            print(*coefficients)
                
                