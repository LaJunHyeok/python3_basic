prompt="""
사칙연산 계산 프로그램입니다.
숫자 형식 및 숫자 연산자로 구하고자 하는 식을 입력해주세요.

입력: """
import re
userinput = input(prompt).strip() 
target = set("+-*/×÷")
#연산자 유효성 체크
if any((c in target) for c in userinput) :
    new_userinput = re.split(r'[+]|[-]|[*]|[/×÷]',userinput) #입력한 숫자값
    if len(new_userinput) > 2:
        print("ERROR: 하나의 연산자만 입력해주세요.")
    else :
        print(round(eval(userinput),3))
else:
    print("ERROR: 연산자를 다시 입력해주세요.")

# 깨달은 교훈 : eval함수를 쓰면 너무너무~ 간편하다! 정규표현식은 공부하장