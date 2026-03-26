import sys

N = int(sys.stdin.readline())
GomGomticon = set()
cnt = 0

for _ in range(N):
    ID = sys.stdin.readline().strip()
    
    if ID == 'ENTER':
        if GomGomticon:
            GomGomticon.clear()
    
    else:
        if ID not in GomGomticon:
            GomGomticon.add(ID)
            cnt += 1

print(cnt)