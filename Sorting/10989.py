import sys

N = int(sys.stdin.readline())
count_array = [0] * 10001

for _ in range(N):
    number = int(sys.stdin.readline())
    count_array[number] += 1

for i in range(10001):
    if count_array[i] != 0:
        for _ in range(count_array[i]):
            print(i)
