import sys

N = int(sys.stdin.readline())
present_set = set()

for _ in range(N):
    people_present = sys.stdin.readline().split()
    people_name = people_present[0]
    people_status = people_present[1]
    
    if people_status == 'enter':
        present_set.add(people_name)
    elif people_status == 'leave':
        present_set.remove(people_name)

reverse_sort_list = sorted(present_set, reverse=True)
print("\n".join(reverse_sort_list))