import sys

data = [i for i in dir(sys) if i[0] != '_']

# for i in data:
#     print(i, '===>\n', i.__doc__, '\n===============')


# data = list(filter(lambda x: True if x[0] != '_' else False, dir(sys)))
# print(data) 

print(sys.executable)
print(sys.platform)
print(sys.argv[0])
print(sys.version_info.major)

print(sys.getsizeof(5))
print(sys.getsizeof('k'))