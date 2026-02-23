import sys

class WordCounter:
    def __init__(self):
        self.cnt = 1

    def Blank_Count(self, X):
    
        words = X.split()
        print(len(words))

if __name__ == "__main__":
    my_wordcounter = WordCounter()
    S = sys.stdin.readline().strip()
    my_wordcounter.Blank_Count(S)