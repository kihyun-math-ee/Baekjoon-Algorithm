import sys

N, K = map(int, sys.stdin.readline().split())
coin_L = []
cnt = 0
for _ in range(N):
    coin = int(sys.stdin.readline())
    coin_L.append(coin)

coin_L.reverse()

for i in range(N):
    if (K // coin_L[i]) != 0:
         cnt += (K // coin_L[i])
         K = (K % coin_L[i])

print(cnt)