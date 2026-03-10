import sys

# BOJ 2231: Decomposition Sum (OOP Architecture / Brute Force)
# Time Complexity: O(1) mathematically bounded near-constant time.
# 
# Engineering Notes:
# 1. Encapsulated the brute-force search algorithm inside an Object-Oriented class structure.
# 2. Mathematical Optimization: Utilizes the universal lower bound of `target - (9 * length)` 
#    to start the search. This prevents mathematical edge-case skipping while bypassing 
#    hundreds of thousands of unnecessary iterations.
# 3. State Management: Employs a boolean flag (`self.sum_exist`) to cleanly handle 
#    the failure state if no valid constructor is found.

class Decomposition_Sum:
    def __init__(self):
        # Initialize state variables
        self.decomposition_sum = 0

    def components_itself(self, target):
        # Calculate the optimal mathematical floor to prevent unnecessary loops
        # We use max(1, ...) to ensure we never check negative numbers
        self.itself = max(1, target - (9 * len(str(target))))
        
        # Flag to track if a valid constructor is found
        self.sum_exist = False
        
        # Search upwards from the lower bound directly to the target
        while target >= self.itself:
            self.all_decomposition = 0
            
            # Sum the individual digits of the current number
            for i in range(len(str(self.itself))):
                self.all_decomposition += int(str(self.itself)[i])
            
            # Check if the number + its digit sum equals the target
            if target != self.all_decomposition + self.itself:
                self.itself += 1
            
            else:
                # The first match is mathematically guaranteed to be the minimum
                self.sum_exist = True
                print(self.itself)
                sys.exit(0)

        # If the loop exhausts all possibilities without finding a match
        if self.sum_exist == False:
            print(0)

if __name__ =='__main__':
    # 1. Instantiate the generator object
    my_decomposition_sum = Decomposition_Sum()
    
    # 2. Read input and execute the bounded exhaustive search
    N = int(sys.stdin.readline())
    my_decomposition_sum.components_itself(N)



    

