import sys

N = int(sys.stdin.readline())
addicted_set = set()
addicted_set.add('ChongChong')

for _ in range(N):
    people_1, people_2 = sys.stdin.readline().split()
    
    if people_1 in addicted_set or people_2 in addicted_set:
        addicted_set.add(people_1)
        addicted_set.add(people_2)

print(len(addicted_set))