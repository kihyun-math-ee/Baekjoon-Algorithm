import sys
students = list(range(1, 31))

for _ in range(28):
    N = int(sys.stdin.readline())
    students.remove(N)

print(min(students))
print(max(students))
        
    
