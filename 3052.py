import sys
module = []
for _ in range(10):
    n = int(sys.stdin.readline())
    m = n % 42
    if m not in module:
        module.append(m)
print(len(module))
