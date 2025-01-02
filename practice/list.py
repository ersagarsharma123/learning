# l1 = [2,4,5,6,7,8]
# print(id(l1))
# l2 = l1.copy()
# print(id(l2))
# print(l2)
import copy


a=10
b=10

print(id(a), id(b))
if a == b:
    print('true')
else:
    print('false')

print('======')

if a is b:
    print('true')
else:
    print('false')