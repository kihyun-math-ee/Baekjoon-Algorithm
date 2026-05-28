Complement = set()

for i in range(1, 10001):
    result = i + sum(map(int, str(i)))
    Complement.add(result)
    
for k in range(1, 10001):
    if k not in Complement:
        print(k)