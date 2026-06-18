import sys

M, N = map(int, sys.stdin.readline().split())
num_dict = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
word_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
target = []
result = []

for i in range(M, N + 1):
    x = str(i)
    word = []
    for j in range(len(x)):
        word.append(num_dict[x[j]])
    target.append(word)

target.sort()

for k in range(0, N - M + 1):
    y = ''
    for element in target[k]:
        y += word_dict[element]
    result.append(y)

cut = (N - M + 1) // 10

for z in range(cut):
    print(*result[10*z:10*(z+1)])
if (N - M + 1) % 10 != 0:
    print(*result[10*cut:])



    