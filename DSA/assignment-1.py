"""1. Given an array with some integer type values. Write a python script to sort array values?"""

# Solution-2===========================================================
import time
import array
start_time = round(time.time()*1000,2)
print(start_time)
arr = array.array('i', [84,61,97,52,45,75,16,1233,19,44,59,86,3,5,78,31,23,68,54,22,8,64,22295,91,10,72,77,89,39,48,56,33,13,80,7,21,66,24,9,99,70,11,42,93,55,36,85,17,40,58])
for i in range(len(arr)-1):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
end_time = round(time.time()*1000,2)
print(end_time)
print('time taken::', round(end_time-start_time,2), 'ms')
print(arr)




# Solution-1===============================================================
"""

import array
import time
start_time = round(time.time(), 3)
arr = array.array('i', [84,61,97,52,45,75,16,1,19,44,59,86,3,5,78,31,23,68,54,22,8,64,95,91,10,72,77,89,39,48,56,33,13,80,7,21,66,24,9,99,70,11,42,93,55,36,85,17,40,58])
# arr = array.array('i', [1,3,2,5,4])
print(arr)

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[i]>arr[j+1+i]:
            arr[i], arr[j+1+i]= arr[j+1+i], arr[i]
            # continue
end_time = (round(time.time(), 3))
print('time_taken = ', round(end_time-start_time,3)*1000, 'ms')
print(arr)

"""

