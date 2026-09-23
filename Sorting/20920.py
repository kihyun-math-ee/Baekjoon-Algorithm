import sys

N, M = map(int, sys.stdin.readline().split())
target_dict = {}
result_list = []

for _ in range(N):
    target = sys.stdin.readline().strip()
    if len(target) >= M:
        if target in target_dict:
            target_dict[target] += 1
        else:
            target_dict[target] = 1
            result_list.append(target)

result_list.sort(key=lambda x: (-target_dict[x], -len(x), x))
print('\n'.join(result_list))