"""4. Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map."""



p = [3,4,5,6]

# result = [0**3, 1**4, 2**5, 3**6]
data = []
for i, j in enumerate(p):
    data.append(i**j)

print(data)


result = list(map(lambda x,y: y**x, p, [0,1,2,3]))
print(result)