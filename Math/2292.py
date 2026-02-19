import sys

def solve():
    N = int(sys.stdin.readline())

    if N == 1:
        print(1)
        return

    limit = int(N**(0.5)) + 2
    
    for i in range(limit):
        upper_bound = 3 * i * (i + 1) + 1
        
        if N <= upper_bound:
            print(i + 1)
            break

if __name__ == "__main__":
    solve()