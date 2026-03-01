import sys

N = int(sys.stdin.readline())
member_list = []
for _ in range(N):
    member = sys.stdin.readline().split()
    member_list.append([int(member[0]), member[1]])

member_list.sort(key=lambda x: int(x[0]))
for i in range(N):
    print(*member_list[i])