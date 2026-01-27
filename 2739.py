import sys

N = int(sys.stdin.readline())

# range(1, 10) -> [1, 10) -> 1부터 9까지 반복
for i in range(1, 10):
    # 출력 형식 주의: 연산자 사이 공백 필수
    print(f"{N} * {i} = {N * i}")
