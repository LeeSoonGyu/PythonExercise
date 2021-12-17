# 1.
su = 5
dan = 800
print(su)
print(dan)
print('su 주소 : ', id(su))
print('dan 주소 : ', id(dan))
price = su*dan
print('금액 : ', price)

# 2.
y = 2.5*x**2+3.3*x+6 # x=2
y = 2.5*2**2+3.3*2+6
print('2차 방정식 결과 : ',y)

# 3.
lee = int(input("지방의 그램을 입력하세요 : "))
soon = int(input("탄수화물의 그램을 입력하세요 : "))
gyu = int(input("단백질의 그램을 입력하세요 : "))
total = lee * 9+ soon * 4+ gyu * 4
print('총 칼로리 : ',total)
# print('총 칼로리 = ', format(total, '3,d'), 'cal')

# 4.
word1 = input("첫번째 단어 : ")
word2 = input("두번째 단어 : ")
word3 = input("세번째 단어 : ")
word4 = input("네번째 단어 : ")
print('='*17)
addr = word1[0]+word2[0]+word3[0]
print(addr)
print('약자 : '+ addr)
print('약자 : ', 'L'+word3.swapcase()[0]+word4.swapcase()[0]+word1[3]) # 대문자변경
# print('약자 : ', word2.swapcase()[-1]+word3.swapcase()[0]+word4.swapcase()[0]+word1[3])