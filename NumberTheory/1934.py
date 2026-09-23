import sys

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    dict_A = {}
    dict_B = {}
    
    i = 2
    temp_A = A
    while temp_A > 1:
        if temp_A % i == 0:
            if i in dict_A:
                dict_A[i] += 1
            else:
                dict_A[i] = 1
            temp_A = temp_A // i
        else:
            i += 1

    i = 2
    temp_B = B
    while temp_B > 1:
        if temp_B % i == 0:
            if i in dict_B:
                dict_B[i] += 1
            else:
                dict_B[i] = 1
            temp_B = temp_B // i
        else:
            i += 1

    lcm = 1
    
    all_primes = set(dict_A.keys()).union(set(dict_B.keys()))
    
    for prime in all_primes:
        power_A = dict_A.get(prime, 0)
        power_B = dict_B.get(prime, 0)
        
        max_power = max(power_A, power_B)
        
        lcm *= (prime ** max_power)

    print(lcm)