import sys

# 속도 최적화를 위해 sys.stdin.readline 사용
x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

# 중첩 조건문으로 비교 횟수 최적화 (Nested If)
if x > 0:
    print(1 if y > 0 else 4)
else:
    print(2 if y > 0 else 3)
