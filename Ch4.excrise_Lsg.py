# 이순규
# 1.
lst = [10, 1, 5, 2]
print(lst)
result = lst*2
print('단계 1 : ', result)
print(result)
len(result)
result.insert(9, result[0]*2)
print('단계 2 : ', result)
print(result)
print(result[1::2])
result2 = result[1::2]
print('단계 3 : ', result2)

# 2.
# 2-1
a = int(input('vector 수 : '))
r = []
for i in range(a) :
    r.append(int(input(3)))
print(r)
print('vector 크기 : ', len(r))

# 2-2
b = int(input('vector 수 : '))
r = []
for i in range(b):
    r.append(int(input(6)))
print(r)
if 5 in r :
    print('Yes')
else :
    print('No')

# 3.
# 3-1
message = ['spam', 'ham', 'spam', 'ham', 'spam']
print(message)
dummy = ['spam' == 1 for dummy in message]
print(dummy)
# 3-2
spam_list = [c for c in message if c == 'spam']
print(spam_list)

# 4.
position = ['과장', '부장', '대리', '사장', '대리', '과장']
oposition = set(position)
print('중복되지 않는 직위 : ', oposition)
po = {}
for key in position:
    po[key] = po.get(key, 0) + 1
print('각 직위별 빈도수 : ', po)