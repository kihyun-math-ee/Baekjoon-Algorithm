import sys
X = int(sys.stdin.readline())
N = 0
# [{(N-1)(N)}/2] + 1 <= X <= {N(N+1)}/2
# if N % 2 = 0, i / 2N - i | if N % 2 = 1, (2N-1) - i / i
while True:
    try:
        N += 1

    except:
        if ((N-1)*(N)//2) + 1 <= X <= (N*(N+1))//2:
            if N % 2 == 0:
                for i in range(N):
                    if X - ((N-1)*(N)//2) + 1 == i:
                        print(f'{i+1}/{2*N-i}')

            elif N % 2 == 1:
                for j in range(N):
                    if X - ((N-1)*(N)//2) + 1 == j:
                        print(f'{((2*N-1)-j)}/{j+1}')
        break
