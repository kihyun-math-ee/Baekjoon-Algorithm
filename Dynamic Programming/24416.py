import sys

cnt = 0
dp_cnt = 0
def fib(n):
    global cnt
    if n == 1 or n == 2:
        cnt += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fibonacci(m):
    global dp_cnt
    f = [0] * (m + 1)
    f[1] = 1
    f[2] = 1
    for i in range(3, m + 1):
        dp_cnt += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[m]

N = int(sys.stdin.readline())
fib(N)
fibonacci(N)
print(cnt, dp_cnt)