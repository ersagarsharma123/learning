"""8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings."""

result = list(map(lambda  x: str(x), [1,2,3,4,5]))
print(result)

result1 = tuple(map(lambda  x: str(x), (1,2,3,4,5)))
print(result1)