import sys

N = int(sys.stdin.readline())
Process = []

def hanoi(num, start, end, aux):
    global Process
    if num == 1:
        Process.append([start, end])
        return
    else:
        hanoi(num - 1, start, aux, end)
        Process.append([start, end])
        hanoi(num - 1, aux, end, start)

hanoi(N, 1, 3, 2)
print(len(Process))
for i in range(len(Process)):
    print(*Process[i])