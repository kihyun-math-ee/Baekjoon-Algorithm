import sys

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
a, b, c, d = map(int, sys.stdin.readline().split())
cnt = 0
result = 0
L = []
M = -1000000001
m = 1000000001

def Operator_Sequence(idx, current_result, add, sub, mul, div):
    global cnt, execution, result, M, m
    if idx == N:
        if current_result >= M:
            M = current_result
        if m >= current_result:
            m = current_result
        return
    
    if add > 0:
        Operator_Sequence(idx + 1, current_result + sequence[idx], add - 1, sub, mul, div)

    if sub > 0:
        Operator_Sequence(idx + 1, current_result - sequence[idx], add, sub - 1, mul, div)

    if mul > 0:
        Operator_Sequence(idx + 1, current_result * sequence[idx], add, sub, mul - 1, div)

    if div > 0:
        if current_result >= 0:
            Operator_Sequence(idx + 1, current_result // sequence[idx], add, sub, mul, div - 1)

        else:
            Operator_Sequence(idx + 1, -(abs(current_result) // sequence[idx]), add, sub, mul, div - 1)

Operator_Sequence(1, sequence[0], a, b, c, d)
print(M)
print(m)



