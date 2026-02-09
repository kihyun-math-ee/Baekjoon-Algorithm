import sys
word = sys.stdin.readline().strip().upper()
unique_chars = list(set(word))
cnt_list = []

for x in unique_chars:
    cnt = word.count(x)
    cnt_list.append(cnt)
    
if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    max_idx = cnt_list.index(max(cnt_list))
    print(unique_chars[max_idx])
     


