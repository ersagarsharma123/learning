# a = [1,2]
# b = [3,4]
# print(a, id(a))
# def add(x,y):
#     x.append(99)
#     return x+y

 
# c = add(a,b)
# print(c)

# print('====')
# print(id(a), a)

# ===========================================
# a=[1,2]
# a = 10
# print(a, id(a))
# def change(x):
#     print(x, id(x))
#     # x.extend([99,88])
#     # x +=[55,66]
#     # x = x + [55,66]
#     x += 50
#     print(x, id(x)) 
#     return x

# change(a)
# print(a, id(a))

# ==============================================================

num1= 10
num2 = num1
print(num1, id(num1) , '?', num2, id(num2))
num1 += 20
print(num1, id(num1) , '?', num2, id(num2))
print('============\n')



num3 = [10,20]
num4 = num3
print(num3, id(num3) , '?', num4, id(num4))
num3 += [30,40]
print(num3, id(num3) , '?', num4, id(num4))


# =======================================================












































