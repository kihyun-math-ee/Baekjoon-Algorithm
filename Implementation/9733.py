import sys

class BeeWork:
    def __init__(self):
        self.cnt_Re = 0
        self.cnt_Pt = 0
        self.cnt_Cc = 0
        self.cnt_Ea = 0
        self.cnt_Tb = 0
        self.cnt_Cm = 0
        self.cnt_Ex = 0
        self.Total_work = 0

    def workspace(self, X):    
        if not X:
            sys.exit(0)

        else:
            for i in range(len(X)):
                if X[i] == "Re":
                    self.cnt_Re += 1
                elif X[i] == "Pt":
                    self.cnt_Pt += 1
                elif X[i] == "Cc":
                    self.cnt_Cc += 1
                elif X[i] == "Ea":
                    self.cnt_Ea += 1
                elif X[i] == "Tb":
                    self.cnt_Tb += 1
                elif X[i] == "Cm":
                    self.cnt_Cm += 1
                elif X[i] == "Ex":
                    self.cnt_Ex += 1
        
            self.Total_work += len(X)

            print(f"Re {self.cnt_Re} {(self.cnt_Re/self.Total_work):.2f}")
            print(f"Pt {self.cnt_Pt} {(self.cnt_Pt/self.Total_work):.2f}")
            print(f"Cc {self.cnt_Cc} {(self.cnt_Cc/self.Total_work):.2f}")
            print(f"Ea {self.cnt_Ea} {(self.cnt_Ea/self.Total_work):.2f}")
            print(f"Tb {self.cnt_Tb} {(self.cnt_Tb/self.Total_work):.2f}")
            print(f"Cm {self.cnt_Cm} {(self.cnt_Cm/self.Total_work):.2f}")
            print(f"Ex {self.cnt_Ex} {(self.cnt_Ex/self.Total_work):.2f}")
            print(f"Total {self.Total_work} 1.00")

if __name__ == "__main__":
    my_beework = BeeWork()
    line = sys.stdin.read().split()
    my_beework.workspace(line)