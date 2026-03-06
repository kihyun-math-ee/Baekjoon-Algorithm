import sys

class Perfect_Num:
    
    def check_perfect(self, target):
        self.factor_list = []
              
        for i in range(1, target):
            if target % i == 0:
                self.factor_list.append(i)
                
        if sum(self.factor_list) == target:
            formula = " + ".join(map(str, self.factor_list))
            print(f"{target} = {formula}")
        else:
            print(f"{target} is NOT perfect.")

if __name__ == "__main__":
    my_perfect_num = Perfect_Num()
    
    while True:
        n = int(sys.stdin.readline())
        if n == -1:
            break
        
        my_perfect_num.check_perfect(n)

    