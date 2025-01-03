from functools import  reduce


list1 = [1,2,3,4,5,6,7,8,9]
def add(x,y):
    return x+y


result = reduce(add, list1, 10)
print(result)


