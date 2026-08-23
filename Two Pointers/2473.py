import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
L.sort()
nearest_neutral = float('inf')
result = []
for i in range(1, N - 1):
    left = i - 1
    right = i + 1
    current_sum = L[left] + L[i] + L[right]
    while left >= 0 and right <= N - 1:
        current_sum = L[left] + L[i] + L[right]

        if abs(current_sum) < nearest_neutral:
            nearest_neutral = abs(current_sum)
            result = [L[left], L[i], L[right]]

        if current_sum < 0:
            right += 1

        elif current_sum > 0:
            left -= 1

        else:
            break
        
result.sort()
print(*result)