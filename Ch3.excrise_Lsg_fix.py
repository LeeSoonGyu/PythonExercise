# Ch3 연습문제 이순규

# 1.
#1)
# 10kg이상이면 수수료 10,000원 10kg 미만이면 수수료 없다.
weight = int(input('짐의 무게는 얼마입니까? : '))
if weight >= 10 :
    print('수수료는 10,000입니다.')
else :
    print('수수료는 없습니다.')
#2)
we = int(input('짐의 무게는 얼마입니까? : '))
if we >= 10 :
    we = int(we / 10) * 10000
    print('수수료는'+format(we)+'입니다.')
else :
    print('수수료는 없습니다.')

# 2.
import random
print('>> 숫자 맞추기 게임 <<')
com = random.randint(1, 10) # 1~10 난수 발생
while True :
    my = int(input('예상 숫자를 입력하세요 : '))
    if my == com :
        print('성공')
        # break
    elif my > com :
        print('더 작은 수를 생각해봐.')
    elif my < com :
        print('더 큰 수를 생각해봐.')

# 3.
soon = 0
for i in range(1, 101) :
    if i % 3 == 0 and i % 2 != 0 :
        print(i, end=' ')
        soon += 1
        print('수열 = '.format(i))
print('\n누적합 = %d' % soon)

# 4.
multiine = """안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""
words = []
for word in multiine.split() :
    words.append(word)
print('\n''단어 : '.join(words))
print('단어 수 : ', len(words))