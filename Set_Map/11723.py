import sys

class set_calculator:
    
    def __init__(self):
        self.target_set = set()
    
    def set_function(self, C):
        if C[0] == 'add':
            self.target_set.add(int(C[1]))

        elif C[0] == 'remove':
            if int(C[1]) in self.target_set:
                self.target_set.remove(int(C[1]))

        elif C[0] == 'check':
            if int(C[1]) in self.target_set:
                print(1)
            else:
                print(0)

        elif C[0] == 'toggle':
            if int(C[1]) in self.target_set:
                self.target_set.remove(int(C[1]))
            else:
                self.target_set.add(int(C[1]))

        elif C[0] == 'all':
            self.target_set = set(range(1, 21))

        elif C[0] == 'empty':
            self.target_set.clear()

if __name__ == '__main__':
    my_set_cal = set_calculator()
    N = int(sys.stdin.readline())

    for _ in range(N):
        sentence = sys.stdin.readline().split()
        my_set_cal.set_function(sentence)


        