"""3. Write a Python function that filters out all elements less than or equal than a specified value from a list of numbers using the filter function."""


result = list(filter(lambda x: True if x<10 else False, [2,4,6,8,10,15,56]))

print(result)