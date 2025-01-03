"""5. Write a Python function that filters out all empty strings from a list of strings using the filter function."""


strings = ['sagar', '', 'is', 'good', '', '', 'boy']

result = list(filter(lambda x: True if x !='' else False, strings))
print(result)