import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
L.sort()
left = 0
right = N - 1
current_sum = L[left] + L[right]
nearest_neutral = abs(current_sum)
target = [L[left], L[right]]

while True:
    if right <= left:
        break

    else:
        if current_sum == 0:
            print(*target)
            sys.exit(0)

        if abs(current_sum) < nearest_neutral:
            nearest_neutral = abs(current_sum)
            target.clear()
            target.append(L[left])
            target.append(L[right])

        if current_sum > 0:
            current_sum = current_sum - L[right] + L[right - 1]
            right -= 1

        elif current_sum < 0:
            current_sum = current_sum - L[left] + L[left + 1]
            left += 1

print(*target)