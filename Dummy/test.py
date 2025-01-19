a = [1, 2, 5, 7, 8, 9] 
b = [1, 2, 3, 5, 8, 10]
result = [i for i in b if i in a]
print(result)

x=lambda y: y**2
print(x(5))
# =====================================

# =======================================
temp=56
print(id(temp))
def temp1():
    global temp 
    print(temp)
    print(id(temp))
    return temp

temp1()
print(temp)