import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

min_val = nums[0]
max_val = nums[0]

for x in nums:
    if x > max_val:
        max_val = x
    elif x < min_val:
        min_val = x

print(min_val, max_val)
