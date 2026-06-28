import sys

target = []
vowel = set(['a', 'e', 'i', 'o', 'u'])
vowel_cnt = 0
consonant_cnt = 0

def password(start, n, m, l):
    global vowel_cnt
    global consonant_cnt
    if len(target) == n:
        if (vowel_cnt >= 1) and (consonant_cnt >= 2):
            print(''.join(target))
        return
    
    for i in range(start, m):
        if l[i] in vowel:
            vowel_cnt += 1
        else:
            consonant_cnt += 1
        target.append(l[i])
        password(i + 1, n, m, l)
        if target[-1] in vowel:
            vowel_cnt -= 1
        else:
            consonant_cnt -= 1
        target.pop()

L, C = map(int, sys.stdin.readline().split())
letter = list(sys.stdin.readline().rstrip().split())
letter.sort()
password(0, L, C, letter)