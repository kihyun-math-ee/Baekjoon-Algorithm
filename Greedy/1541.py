import sys

S = sys.stdin.readline().strip()
min_sum = 0
num = ''
total = 0
operator = []

for i in range(len(S)):
    if (S[i] != '-') and (S[i] != '+'):
        num += S[i]
        if i == (len(S) - 1):
            if '-' in operator:
                total -= int(num)
            else:
                total += int(num)


    elif S[i] == '-':
        if '-' not in operator:
            total += int(num)
            num = ''
            operator.append('-')
        else:
            total -= int(num)
            num = ''

    elif S[i] == '+':
        if '-' in operator:
            total -= int(num)
            num = ''
        else:
            total += int(num)
            num = ''

print(total)
        
