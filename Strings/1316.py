import sys

class Group_voca:
    
    def __init__(self):
        self.cnt = 0

    def is_group_check(self, X):
        
        self.group_voca_check = True
        self.group_list = [0] * 127

        for i in range(len(X)):
            if self.group_list[ord(X[i])] == 0:
                self.group_list[ord(X[i])] = 1
            elif self.group_list[ord(X[i])] == 1:
                if X[i] != X[i-1]:
                    self.group_voca_check = False
                    break
        if self.group_voca_check == True:
            self.cnt += 1
            
    def result(self):
        print(self.cnt)
        
                
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    my_group_voca = Group_voca()
    for _ in range(N):
        word = sys.stdin.readline().strip()
        my_group_voca.is_group_check(word)

    my_group_voca.result()
