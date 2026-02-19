import sys

def solve():
    N = int(sys.stdin.readline())
    
    side_points = 2
    
    for _ in range(N):
        side_points = 2 * side_points - 1

    print(side_points ** 2)

if __name__ == "__main__":
    solve()