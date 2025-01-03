"""2. Write a Python program to add three given lists using Python map and lambda."""

result = list(map(lambda a,b,c:a+b+c , [1,2], [3,4], [5,6]))
print(result)
