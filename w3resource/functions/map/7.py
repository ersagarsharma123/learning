"""7. Write a Python program to add two given lists and find the difference between them. Use the map() function."""

#adding
list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
result = list(map(lambda x,y:x+y, list1, list2))
print(result)

#difference
result2 = list(map(lambda x,y:x-y, list1, list2))
print(result2)