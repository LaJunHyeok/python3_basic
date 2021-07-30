"""
 문제: 반복문을 이용하여 입력받은 정수만큼, 입력받은 정수 출력
  정수가 아니라면 오류 메세지 출력
  입력을 받을때 "숫자를 입력하세요." 라는 메세지를 띄워야 합니다

  예> 5 입력시 5 5 5 5 5 출력
"""

userinput = input("숫자를 입력하세요. :")
try:
    cnt = int(userinput)
    for i in range(0,cnt):
        print(userinput)
except ValueError:
    print("ERROR: '정수'를 입력해주세요.")


