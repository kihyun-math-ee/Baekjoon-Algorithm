import sys

N = int(sys.stdin.readline())
target_dict = {}
target_list = []

for _ in range(N):
    num = int(sys.stdin.readline())
    target_list.append(num)

    if num in target_dict:
        target_dict[num] += 1

    else:
        target_dict[num] = 1

target_list.sort()
max_val = max(target_dict.values())
max_keys = [k for k, v in target_dict.items() if v == max_val]
max_keys.sort()

if len(max_keys) == 1:
    mode = max_keys[0]

else: 
    mode = max_keys[1]

arithmetic_mean = round(sum(target_list) / N)
median = target_list[(N - 1) // 2]
target_range = target_list[-1] - target_list[0]

print(arithmetic_mean)
print(median)
print(mode)
print(target_range)
