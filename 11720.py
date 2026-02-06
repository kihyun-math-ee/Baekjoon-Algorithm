import sys
N = int(sys.stdin.readline())
M = sys.stdin.readline().strip() 
total = 0

for x in M:      
    total += int(x)
print(total)
