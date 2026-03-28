import sys

def cantor_set(length, result, start):
    if length == 1:
        return result
    else:
        result[start + (length // 3):start + (length // 3) * 2] = [' '] * (length // 3)
        cantor_set((length // 3), result, start)
        cantor_set((length // 3), result, start + (length // 3) * 2)
        return result

while True:
    try:
        N = int(sys.stdin.readline())
        target = ['-'] * (3 ** N)
        print(''.join(cantor_set(3 ** N, target, 0)))
    
    except ValueError:
        break
    
