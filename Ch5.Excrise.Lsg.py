# 1.
def StarCount(height):
    if height == 0:
        return 0
    else:
        result = height + StarCount(height-1)
        print('*'*height)
        return result
height = int(input('height : '))
print('start 개수 :', StarCount(height))


# 2.
def bank_account(num):
    balance = num
    def getbalance(): # 최초금액
        return balance
    def deposit(money): # 입금
        nonlocal balance
        balance += money
        # print('입금액 : ', money) # 입금액 출력
    def withdraw(money): #출금
        nonlocal balance
        balance -= money
        # print('출금액 : ', money) # 출금액 출력
        if balance < money:
            print('잔액이 부족합니다.')
    return getbalance, deposit, withdraw

getbalance, deposit, withdraw = bank_account(1000)
print('최초의 계좌의 잔액은 : ', getbalance(), '원입니다')
print('현재 계좌 잔액은 : ', getbalance(), '원입니다')
deposit(15000)
print('입금액을 입력하세요 : ', (getbalance()-1000), '원입니다')
# print('입금액을 입력하세요 : ', (getbalance()), '원입니다')
print('입금후 잔액은 : ', (getbalance()), '원입니다')
withdraw(3000)
print('출금액을 입력하세요 : ', (getbalance()-10000), '원입니다')
print('3000원 출금 후 잔액은 : ', (getbalance()), '원입니다')
withdraw(30000) # 잔액부족 메세지 등장

# 3.
def Factorial(n):
    if n == 1:
        return 1
    else :
        result = n * Factorial(n-1)
        return result

result_fact = Factorial(5)
print('패토리얼 결과 = ', result_fact)