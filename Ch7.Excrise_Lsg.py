# 연습문제 이순규
# 1. email 양식 처리조건
# 1). 아이디 : 첫자는 영문소문자, 단어길이 4자 이상
# 2). 호스트 이름 : 영문소문자 시작, 단어길이 3자 이상
# 3). 최상위 도메인 : 영문소문자 3자리 이하
# 4). 정규표현식 기본 패턴 : '메타문자@메타문자.메타문자'
multi_line = """hong@12.com
you2@naver.com
12kang@hanmail.net
kimjs@gmail.com"""
from re import findall, match
for i in multi_line.split(sep='\n') :
    result = findall('^[a-z]\w{3,}@[a-z]{3,}.[a-z]{,3}', i) #\\w 단어 [0-9a-zA-Z_]와 같다. 영문자+숫자+밑줄 등등..
    if result :
        print('일치 도메인 주소 : ', result)
    else:
        print('불일치 도메인 주소')

# 2.
# emp 변수 이용 사원의 이름만 추출하는 함수 정의
from re import findall
emp = ['2014홍길동220', '2020이순신300', '2010유관순260']
def name_pro(emp):
    names = []
    for i in emp :
        name = findall('[가-힣]{3}', i)
        names += name
        # names.append(name[0])
    return names
names = name_pro(emp)
print('names = ', names)

# 3.
# emp 변수 이용 사원의 급여 평균 추출 함수 정의
from re import findall
from statistics import mean
emp = ['2014홍길동220', '2020이순신300', '2010유관순260']
pays = []
def pay_pro(emp):
    for i in emp :
        name = findall('[가-힣][0-9]{3}', i)
        pay = findall('[0-9]{3}', name[0])
        pays.append(int(pay[0]))
    return pays
pays = pay_pro(emp)
print(pays)
print('급여 평균 : ', mean(pays))

# 4.
# emp 변수를 이용 전체 급여평균 / 평균이상 급여 수령자 추출 함수 정의
from re import findall
from statistics import mean

emp = ['2014홍길동220', '2002이순신300', '2010유관순260']
names=[]
pays=[]
def pay_pro2(emp):
    for i in emp:
        name = findall('[가-힣]{3}',i)
        names.append(name[0])
        name = findall('[가-힣][0-9]{3}', i)
        pay = findall('[0-9]{3}', name[0])
        pays.append(int(pay[0]))
pay_pro2(emp)
print('전체사원급여평균:', mean(pays))
print('평균 이상 급여 수령자')
a=names
for b in pays:
    if b >= (mean(pays)):
        print(a[pays.index(b)],'=>',b)

# 5.
# 전처리
from re import findall, sub
texts = ['AFAB54747,asabag?', 'abTTa$$;a12:2424.', 'uysfsfA,A123&***$?']
# 단계 1 : 소문자 변경
texts_re = [t.lower() for t in texts]
# print('texts_re : ', texts_re)
# 단계 2 : 숫자 제거
texts_re1 = [sub('[0-9]', ' ', text)for text in texts_re]
# print('texts_re1 : ', texts_re1)
# 단계 3 : 문장 부호 제거
texts_re2 = [sub('[,.?!:;]', '', text)for text in texts_re1]
# print('texts_re2 : ', texts_re2)
# 단계 4 : 특수 문자 제거 re.sub() 이용
spec_str = '[@#$%^&*()]'
texts_re3 = [sub(spec_str, '', text)for text in texts_re2]
# print('texts_re3 : ', texts_re3)
# 단계 5 : 공백 제거
texts_re4 = [''.join(text.split())for text in texts_re3]
print('texts_re4 : ', texts_re4)


