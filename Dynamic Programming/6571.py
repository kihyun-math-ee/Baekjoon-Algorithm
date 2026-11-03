import sys

dp = [0] * 1000
dp[1] = 1
dp[2] = 2

for i in range(3, 1000):
    dp[i] = dp[i - 1] + dp[i - 2]

while True:
    a, b = map(int, sys.stdin.readline().split())
    cnt = 0

    if a == 0 and b == 0:
        break
    
    else:
        for j in range(1, 1000):
            if  a <= dp[j] <= b:
                cnt += 1
            elif dp[j] > b:
                break
        
        print(cnt)