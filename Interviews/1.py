# ip = [1,[[[2,[3]]],4,5,6]]
# op = [1,2,3,4,5,6]
# op2 = []
# def expand(ip):
#     for i in ip:
#         if type(i) == list:
#             expand(i)
#         else:
#             op2.append(i)
#     return op2
# expand(ip)
# print(op2)

# ===================================================

# ===================================

# test = 'aabbc@dce'  #find 1st non repetative letter from text excluding special character

# test1 = ''.join([i for i in test if i.isalpha()])
# print(test1)

# for i in range(len(test1)):
#     if i == 0:
#         if test1[i] == test1[i+1]:
#             continue
#     elif i == len(test1)-1:
#         if test1[i] != test1[i-1]:
#             print(test1[i])
#     elif test1[i-1] == test1[i] or test1[i] == test1[i+1]:
#         continue
#     else:
#         print(test1[i])


# =========================================================



def multi(a,b,c=1):
    return a*b*c

data1 = multi(5,"3")

print(data1)

print(1^2)


    