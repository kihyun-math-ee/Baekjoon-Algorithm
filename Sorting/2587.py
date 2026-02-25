import sys

List_N = []
for _ in range(5):
    N = int(sys.stdin.readline())
    List_N.append(N)

sorted_List_N = sorted(List_N)
print(sum(List_N)//5)
print(sorted_List_N[2])
