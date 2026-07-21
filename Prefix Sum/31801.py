import sys

L = []

def make_increasing(global_max1):
    result1 = []

    def dfs1(start, path):
        if path:
            result1.append(path[:])

        for i in range(start, global_max1):
            path.append(i)
            dfs1(i + 1, path)
            path.pop()

    dfs1(1, [])
    return result1

def make_decreasing(global_max2):
    result2 = []

    def dfs2(start, path):
        if path:
            result2.append(path[:])

        for j in range(start - 1, -1, -1):
            path.append(j)
            dfs2(j, path)
            path.pop()

    dfs2(global_max2, [])
    return result2

for peak in range(2, 10):
    left_parts = make_increasing(peak)
    right_parts = make_decreasing(peak)

    for left in left_parts:
        for right in right_parts:
            mountain_list = left + [peak] + right
            mountain_num = int("".join(map(str, mountain_list)))
            L.append(mountain_num)

L.sort()
prefix_sum = [0] * (1000001)

for num in L:
    if num <= 1000000:
        prefix_sum[num] = 1

for k in range(1, 1000001):
    prefix_sum[k] = prefix_sum[k - 1] + prefix_sum[k]

T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    result = prefix_sum[b] - prefix_sum[a - 1]
    print(result)
