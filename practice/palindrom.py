string = 'sagar'

# Slice method
reverse_string = string[::-1]
print('string =', string, '\nreverse_string =', reverse_string, "\n================")


#reverse through loop
rev_str = ''
for i in range(len(string)-1, -1,-1):
    rev_str += string[i]
print("for loop=>", rev_str + '')

#while loop
i=len(string)
rev_str1 = ''
while 0<i:
    i-=1
    rev_str1+=string[i]
print("while loop=>",rev_str1)

#inbuilt list reverse
string_list = [*string]
string_list.reverse()
print("list reverse=>",''.join(string_list))

#inbuilt reversed key
rev_str2= reversed([*string])
print('reversed key=>',''.join(list(rev_str2)))


#using reduce
from functools import reduce
rev_str3 = reduce(lambda x,y: y+x, string)
print('reduce=>', rev_str3)













    