import sys

N = int(sys.stdin.readline())
my_card_set = set(sys.stdin.readline().split())
M = int(sys.stdin.readline())
target_card_list = sys.stdin.readline().split()

for x in target_card_list:
    
    if x in my_card_set:
        print(1, end=' ')
    
    else:
        print(0, end=' ')