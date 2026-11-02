import sys

target = []
min_result = float('inf')
num = []

def simillar_gaussian(integer, string):
    global min_result
    if len(target) == len(string):
        if int(''.join(target)) > integer:
            if int(''.join(target)) < min_result:
                min_result = int(''.join(target))
        return
    
    for i in range(len(string)):
        if i not in num:
            target.append(string[i])
            num.append(i)
            simillar_gaussian(integer, string)
            num.pop()
            target.pop()

X = int(sys.stdin.readline())
str_X = str(X)
simillar_gaussian(X, str_X)

if min_result == float('inf'):
    print(0)
else:
    print(min_result)