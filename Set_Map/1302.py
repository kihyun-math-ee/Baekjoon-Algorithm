import sys

bookcnt = {}
N = int(sys.stdin.readline())

for _ in range(N):
    S = sys.stdin.readline().strip()
    
    if S not in bookcnt:
        bookcnt[S] = 1

    else:
        bookcnt[S] += 1

sorted_books = sorted(bookcnt.items(), key=lambda x: (-x[1], x[0]))
print(sorted_books[0][0])
