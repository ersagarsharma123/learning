"""1. Write a Python function that filters out even numbers from a list of integers using the filter function."""

a=[1,2,3,4,5,6,7,8,9]

def even(x):
    if x%2 == 0:
        return True
    else:
        return False
    
result = list(filter(even, a))
print(result)



result1 = list(filter(lambda x:x%2==0, a))
print(result1)
