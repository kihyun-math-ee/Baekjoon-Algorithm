import sys
from collections import deque

class Nqueue:
    def __init__(self, N):
        self.ndeq = deque()
        self.N = N

    def buffer(self, X):
        if X > 0:
            if len(self.ndeq) < self.N:
                self.ndeq.append(X)

        elif X == 0:
            if self.ndeq:
                self.ndeq.popleft()

    def result(self):
        if not self.ndeq:
            print('empty')
        else:
            print(*self.ndeq)
            

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    my_nqueue = Nqueue(n)
    while True:
        target = int(sys.stdin.readline())
        if target == -1:
            break
        else:
            my_nqueue.buffer(target)

    my_nqueue.result()
                