import math
import time
import re
prompt="""
사칙연산 계산 프로그램입니다.
실행하시려면 1을 입력해주세요.

1. Run
2. Quit

Enter number: """
flag = True
while flag:
    res = ''
    userinput = input(prompt)
    if userinput=='1':
        print("===계산기===\n\nC를 입력하면 입력값이 초기화됩니다.\n\n결과조회는 '='을 단독으로 입력해주세요!\n")
        while flag:
            datainput = input("="+res).lower().strip()
            if 'c' in datainput :
                res = ''
                continue
            elif len(re.findall(r'[a-zA-Z]',datainput))>0:
                print("잘못된 문자열이 있습니다. 다시 입력해주세요.")
                continue
            elif '' == datainput:
                continue
            if '=' != datainput: #계산식 중첩 중
                res = res+datainput
                continue
            elif '=' == datainput: #결과출력 누를 때
                res = str(math.floor(eval(res)))
                print(res)
                time.sleep(0.5)
                break
    elif userinput=='2':
        flag=False
    else:
        print("잘못된 입력입니다.")
print("프로그램 종료되었습니다.")
