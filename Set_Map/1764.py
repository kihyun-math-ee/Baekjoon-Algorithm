import sys

N, M = map(int, sys.stdin.readline().split())
never_heard_set = set()
never_seen_set = set()

for _ in range(N):
    never_heard = sys.stdin.readline().strip()
    never_heard_set.add(never_heard)

for _ in range(M):
    never_seen = sys.stdin.readline().strip()
    never_seen_set.add(never_seen)

intersection_set = never_heard_set & never_seen_set

sorted_result = sorted(intersection_set)

print(len(sorted_result))
print('\n'.join(sorted_result))