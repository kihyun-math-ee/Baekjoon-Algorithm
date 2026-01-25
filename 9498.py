x = int(input()) # 입력받은 점수 

  

if x >= 90:  

# [Logic 1] 100점 초과는 입력되지 않으므로(제한 조건), 굳이 x <= 100을 쓸 필요 없음. 

# [Syntax] if문은 x=... 과 동등한 레벨(메인 로직)이므로 들여쓰지 않고 맨 왼쪽에 붙임! 

    print("A") 

elif x >= 80: 

# [Logic 2 - 핵심] 위(if)에서 90 이상은 이미 걸러짐!  

# 따라서 여기까지 내려왔다는 건 이미 '90 미만'이 확정된 상태임. (굳이 x < 90 안 써도 됨) 

    print("B") 

elif x >= 70: 

    print("C") 

elif x >= 60: 

    print("D") 

else: 

    print("F") 