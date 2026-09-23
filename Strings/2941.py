import sys

class Croatian:
    def __init__(self):
        self.croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
        
    def Replace(self, alphabet):
        for i in range(len(self.croatian)):
            alphabet = alphabet.replace(self.croatian[i], 'X')
        print(len(alphabet))

    
if __name__ == "__main__":
    my_croatian = Croatian()
    S = sys.stdin.readline().strip()
    my_croatian.Replace(S)