import pandas as pd
import numpy as np
import os
import sys

# 데이터 칼럼 셋
column_name = ['나이','성별','잔고','결혼여부']

# 데이터 셋 
df_list = [[20,'남자',2000,'미혼'],
    [48,'남자',20000,'결혼'],
    [32,'여자',800,'미혼'],
    [28,'남자',1200,'결혼'],
    [38,'여자',3500,'결혼']]

# 데이터셋을 데이터프레임으로 변환
df = pd.DataFrame(df_list,columns=column_name)
print(df.head()) # head()와 tail() 을 통해 데이터의 위,아래서부터 몇개까지 볼지 정할 수 있다 default=5 이다.

print(os.getcwd()) # 현재 경로 출력
df.to_csv('test.csv',index=False, encoding='utf-8-sig') # 데이터 저장하기 인코딩 안넣으면 한글 깨짐
df = pd.read_csv('test.csv') # 데이터 불러오기
df.head()

df.info() # 타입 .. 데이터프레임의 종합 정보 (특정 컬럼에 대한 이름과 null값의 갯수, 데이터 타입에 대한 정보를 보여준다. even though size of dataframe!)
df.dtypes # data type  형태만 보고 싶을경우 쓰는 함수
df.shape # 형태 .. 데이터 프레임이 몇 행 몇 열인지 정확하게 알고 싶을 때 쓴다.

# describe() 함수 사용 예제
print("==========================================")
print(df.describe()) # 연속형 개략적 분포
df['나이'].describe() # 컬럼(연속형)에 사용할 수도 있다.

# 컬럼 값 분포
# 가장 자주 쓰이는 함수 중 하나! df에도 사용 가능하나, 보통은 컬럼의 값별로 count 하기 위해서 쓰인다.
df['나이'].value_counts() # 컬럼 값 분포(기본값:내림차순)
df['나이'].value_counts(ascending=True) # 오름차순으로 변경

# 위의 값의 인덱스가 보여지는 순서대로 필요할 경우
df['나이'].value_counts().index # 시리즈 인덱스 . 해당 값은 tolist 라는 함수를 사용하여 list 의 객체로도 만들 수 있다.
newlist = list()
newlist = df['나이'].value_counts().index.tolist()

