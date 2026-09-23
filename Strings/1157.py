import sys

class Most:
    def __init__(self):
        self.alphabet = [0] * 26

    def Count(self, letters):
        self.modified_letters = letters.upper()
        
        for i in range(len(self.modified_letters)):
            self.alphabet[ord(self.modified_letters[i]) - ord("A")] += 1

        self.max_count = max(self.alphabet)
        self.duplication_count = 0

        for j in range(26):
            if self.alphabet[j] == self.max_count:
                self.duplication_count += 1
        

        if self.duplication_count > 1:
            print("?")

        else:
            winner_index = self.alphabet.index(self.max_count)
            print(chr(winner_index + ord('A')))

if __name__ == "__main__":
    my_most = Most()
    S = sys.stdin.readline().strip()
    my_most.Count(S)

     


