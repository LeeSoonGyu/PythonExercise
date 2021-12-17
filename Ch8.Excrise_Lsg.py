# 연습문제 이순규
# 1. ftest.txt 파일을 읽고 줄 수와 단어 수를 카운트 하시오.
# 1). 문장은 '\n'을 구분자로 한다
# 2). 단어는 공백을 구분자로한다.
import os
os.getcwd()
file = open('ch08_data/data/ftest.txt', mode='r')
lines = file.readlines()
print(lines)
docs = []
words = []
for line in lines:
    print(line.strip())
    docs.append(line.strip())
    for word in line.split('\n'):
        words.append(word)
print(docs)
print('문장 수 : ', len(docs))
print(words)
print('단어 수 : ', len(words)) # 아무리 수정해도 저는 11개입니다.

# 2. emp.csv파일을 읽고 다음과 같이 출력하시오
# 관측치 길이 : 5
# 전체 평균 급여 370.0
# 최저 급여 : 150, 이름 : 홍길동
# 최고 급여 : 500, 이름 : 강감찬
import pandas as pd
emp = pd.read_csv('ch08_data/data/emp.csv', encoding='utf-8')
print(emp.info())
print(emp.head())

name = emp.Name
pay = emp.Pay

# 1. 관측치 길이
print(emp)
print('관측치 길이 : ', len(emp))

# 2. 전체 평균 급여
from statistics import mean
print('전체 평균 급여 : ', round(mean(pay)))

# 3. 최저 급여 / 최고 급여
print('max pay = ', max(pay))
print('min pay = ', min(pay))
for i in range(len(pay)):
    if pay[i] == min(pay) :
        print('최저 급여 : %d, 이름 : %s' % (min(pay), name[i]))
    if pay[i] == max(pay) :
        print('최저 급여 : %d, 이름 : %s' % (max(pay), name[i]))