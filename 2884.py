import sys

# 속도 최적화를 위해 sys.stdin.readline 사용
H, M = map(int, sys.stdin.readline().split())

# 모든 시간을 '분(minute)' 단위로 환산하여 45분을 뺌
# (H * 60 + M) - 45
total_min = H * 60 + M - 45

# 음수가 될 경우(예: 0시 30분 -> -15분)를 대비해 하루(24*60=1440분)를 더해서 모듈로 연산
# 파이썬의 % 연산자는 음수 처리를 자동으로 양수로 변환해주지만, 명시적으로 처리
if total_min < 0:
    total_min += 24 * 60

# 다시 시/분으로 변환
print(total_min // 60, total_min % 60)
