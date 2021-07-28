
prompt = """

#선별기준
FW = 오버롤 65 이상 컨디션 50이상 주급 2000 이하 일경우 합격
MF = 오버롤 80 이상 컨디션 77이상 주급 1250이하 일경우 합격
DF = 오버롤 75 이상 컨디션 70 이상 주급 1500 이하 일경우 합격
GK = 오버롤 50 이상 컨디션 60이상 주급 1000 이하 일경우 합격

입력 """
question = ["이름: ","오버롤: ","컨디션: ","포지션: ","주급: "]
import time 
inputstatus = ['','','','','']
print(prompt)
time.sleep(0.5)
for i in question :
    print(i , end=' ')
    inputstatus[question.index(i)] = input()
new_inputstatus = [i.strip().upper() for i in inputstatus]
if len(inputstatus) != 5:
    print("ERROR: ','기준 5개의 정보만 입력해주세요.")
elif new_inputstatus[1].isdigit() == False:
    print("ERROR: 오버롤은 숫자형식으로 입력해야합니다.")
elif new_inputstatus[2].isdigit() == False:
    print("ERROR: 컨디션은 숫자형식으로 입력해야합니다.")
elif new_inputstatus[4].isdigit() == False:
    print("ERROR: 주급은 숫자형식으로 입력해야합니다.")
else :    
    position = new_inputstatus[3]
    result = '' 
    if position == 'FW':
        if int(new_inputstatus[1])>=65 and int(new_inputstatus[2]) >= 50 and int(new_inputstatus[4]) <= 2000:
            result = '합격'
        else :
            result = '불합격'
    elif position == 'MF':
        if int(new_inputstatus[1])>=80 and int(new_inputstatus[2]) >= 77 and int(new_inputstatus[4]) <= 1250:
            result = '합격'
        else :
            result = '불합격'
    elif position == 'DF':
        if int(new_inputstatus[1])>=75 and int(new_inputstatus[2]) >= 70 and int(new_inputstatus[4]) <= 1500:
            result = '합격'
        else :
            result = '불합격'
    elif position == 'GK':
        if int(new_inputstatus[1])>=50 and int(new_inputstatus[2]) >= 60 and int(new_inputstatus[4]) <= 1000:
            result = '합격'
        else :
            result = '불합격'
    else :
        print("ERROR: 정확한 포지션을 입력해주세요.")
    if result != '':
        print("{0}는 {1}입니다." .format(new_inputstatus[0],result))