import sys
while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    L = []
    total = 0

    for i in range(1, n):
        if n % i == 0:
            L.append(i)

    for j in range(len(L)):
        total += L[j]

    if n == total:
        formula = " + ".join(str(x) for x in L)
        print(f"{n} = {formula}")

    elif n != total:
        print(f"{n} is NOT perfect.")

    