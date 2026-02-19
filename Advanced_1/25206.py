import sys

class GPA:
    def __init__(self):
        self.dict_gpa = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, 
                         "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

    def get_score(self, credit, grade):
        return credit * self.dict_gpa[grade]

if __name__ == "__main__":
    my_calculator = GPA() 
    
    total_credits = 0.0
    total_score = 0.0
    
    for _ in range(20):
        line = sys.stdin.readline().split()
        if not line: break
        
        credits = float(line[1])
        grade = line[2]
        
        if grade == 'P':
            continue
        
        total_credits += credits
        total_score += my_calculator.get_score(credits, grade)
    
    if total_credits == 0:
        print(0.0)
    else:
        print(total_score / total_credits)