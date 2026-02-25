import sys

# BOJ 1436: Movie Director Shom
# Logic: Brute Force (Sequential Search)

N = int(sys.stdin.readline())
cnt = 0
num = 666 # Optimization: We know the first answer is 666

while True:
    if '666' in str(num):
        cnt += 1
    
    if cnt == N:
        print(num)
        break # CRITICAL: Stop the program immediately!
    
    num += 1


    