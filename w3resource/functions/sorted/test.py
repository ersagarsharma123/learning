list1 = [5,6,97,5,2,3,6,98,4]

#using sort list method
students = [
    {"name": "John", "age": 12},
    {"name": "Aarti", "age": 8},
    {"name": "Deepak", "age": 15},
    {"name": "David", "age": 11},
    {"name": "Karthik", "age": 9},
    {"name": "Kavita", "age": 5},
    {"name": "Jim", "age": 6},
    {"name": "Sourav", "age": 16}
    ]


students.sort(key=lambda x:x['age'])
# print(students)


# =======================================================================================
#using sorted key
students1 = [
    {"name": "John", "age": 12},
    {"name": "Aarti", "age": 8},
    {"name": "Deepak", "age": 15},
    {"name": "David", "age": 11},
    {"name": "Karthik", "age": 9},
    {"name": "Kavita", "age": 5},
    {"name": "Jim", "age": 6},
    {"name": "Sourav", "age": 16}
    ]

data = sorted(students1, key=lambda x: x['age'])
# print(data)
# print(students1)

# ================================================================================================
# generic method
students2 = [
    {"name": "John", "age": 12},
    {"name": "Aarti", "age": 8},
    {"name": "Deepak", "age": 15},
    {"name": "David", "age": 11},
    {"name": "Karthik", "age": 9},
    {"name": "Kavita", "age": 5},
    {"name": "Jim", "age": 6},
    {"name": "Sourav", "age": 16}
    ]

for i in range(len(students2)):
    for j in range(len(students2)-1-i):
        if students2[i].get('age') > students2[i+1+j].get('age'):
            students2[i], students2[i+1+j]= students2[i+1+j], students2[i]

print(students2)


























