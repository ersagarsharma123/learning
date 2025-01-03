"""4. Write a Python program that creates a list of names and uses the filter function to extract names that start with a vowel (A, E, I, O, U)."""

names = ['sagar', 'oyi', 'illi', 'oyus', 'deepak', 'Uganda']
vowels = ['A', 'E', 'I', 'O', 'U']

result = list(filter(lambda x: True if x[0].upper() in vowels else False, names))

print(result)
