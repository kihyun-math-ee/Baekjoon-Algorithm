import sys

A, B, C = map(int, sys.stdin.readline().split())

# 1. 3개 모두 같은 경우
if A == B == C:
    print(10000 + A * 1000)
# 2. 2개만 같은 경우 (A가 B 또는 C와 같으면 겹치는 눈은 A)
elif A == B or A == C:
    print(1000 + A * 100)
# 2-1. 남은 경우 중 B와 C가 같은 경우
elif B == C:
    print(1000 + B * 100)
# 3. 모두 다른 경우 (max 함수 활용)
else:
    print(max(A, B, C) * 100)
