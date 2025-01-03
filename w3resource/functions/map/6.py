"""6. Write a Python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence. Use the map() function."""

char = ('a', 'B', 'v', 'H')

result = list(map(lambda x:(str(x).upper(), str(x).lower()), char))
print(result)