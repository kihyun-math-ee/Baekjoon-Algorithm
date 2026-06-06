import sys

X = int(sys.stdin.readline())
binary_str = bin(X)
binary_str = binary_str[2:]
cnt = 0

for element in binary_str:
    if element == '1':
        cnt += 1

print(cnt)