import sys

class ReverseString:
    def __init__(self):
        pass

    def rev(self, S):
        self.i = 0
        self.j = 0
        self.L = []
        while True:
            if self.j == len(S):
                self.L.append((S[self.i:self.j][::-1]))
                break   
            elif S[self.j] == ' ':
                self.L.append((S[self.i:self.j][::-1]))
                self.i = self.j + 1
                self.j += 1
            else:
                self.j += 1
        print(*self.L)

if __name__ == '__main__':
    my_reversestring = ReverseString()

    N = int(sys.stdin.readline())
    for _ in range(N):
        s = sys.stdin.readline().rstrip()
        my_reversestring.rev(s)
    