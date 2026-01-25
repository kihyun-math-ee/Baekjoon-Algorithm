A, B = map(int, input().split()) # 1단계: 문자열 입력 -> 쪼개기 -> 정수로 변환(매핑) 

  

if A > B:          # 중요: 조건문 끝에는 반드시 콜론(:) 필수! 

    print(">")     # 큰따옴표("")는 문자열 그 자체를 출력 

elif A < B:        # Python에서는 else if 대신 'elif'를 사용 

    print("<") 

else:              # 중요: else 뒤에도 콜론(:) 필수! 

    print("==") 