"""2. Write a Python program that uses the filter function to extract all uppercase letters from a list of mixed-case strings."""

a=['SaGar', 'Is', 'A', 'good', 'Boy']
b=['a', 'V', 'H', 'l']

def uppercase(x:str):
    if x.isupper():
        return True
    else:
        return False



result = list(filter(uppercase, b))
print(result)


def uppercase1(x:str):
    temp = ''
    for i in x:
        if i.isupper():
            temp = temp+i
    return temp

result1 = list(map(uppercase1, a))
print(result1)
      
uppercase_letters = list(filter(lambda char: char.isupper(), ''.join(a)))

print(uppercase_letters)

