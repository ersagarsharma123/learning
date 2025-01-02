"""37. Write a Python program that displays your name, age, and address on three different lines."""

def personal_details(name:str, age:int, add:str):
    name , age, add = name , age, add
    return print("{}\n{}\n{}".format(name, age, add))
personal_details('sagar sharma', 30, 'Kalyan Mumbai')

