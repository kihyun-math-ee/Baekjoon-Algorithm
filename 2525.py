import sys

# 속도 최적화를 위해 sys.stdin.readline 사용
A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

# 모든 시간을 분 단위로 환산
# 중복 연산((A*60)+B+C) 제거하여 변수에 저장
total_min = A * 60 + B + C

# % 24를 통해 24시 초과 시 0부터 순환되도록 처리 (if문 제거)
# (total_min // 60) % 24 : 시(hour)
# total_min % 60 : 분(minute)
print((total_min // 60) % 24, total_min % 60)
