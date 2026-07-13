import sys

L_X = set()
L_Y = set()
L_Z = set()

def string_set(S, t, r, start, target_set):
    if len(t) == r:
        target_set.add("".join(t))
        return
    
    for i in range(start, len(S)):
        t.append(S[i])
        string_set(S, t, r, i + 1, target_set)
        t.pop()

X = sorted(sys.stdin.readline().strip())
Y = sorted(sys.stdin.readline().strip())
Z = sorted(sys.stdin.readline().strip())
k = int(sys.stdin.readline())

string_set(X, [], k, 0, L_X)
string_set(Y, [], k, 0, L_Y)
string_set(Z, [], k, 0, L_Z)

result = list((L_X & L_Y) | (L_X & L_Z) | (L_Y & L_Z))
result.sort()

if not result:
    print(-1)

else:
    for j in result:
        print(j)