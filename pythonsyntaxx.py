# name = 'ajo'
# print(name);

# #Name
# age = 25 #integer
# price = 99.99 #float
# temperature = -10.5 #nagative float

#string
name ="Alice" #Double Quotes
city = 'New york' #single quote
message = """Multiple line strings""" #triple quote

# #boolean
# is_active = True 
# has_error = False

# #none(null value)
# result = None

# #checking data type
# print(type(age)) #<class "int">
# print(type(price)) #<class"float">
# print(type(name)) #<class"str">

# #busic
# addition = 10 + 5
# print(type(addition))
# subtraction = 10 - 5
# multiplication  = 10 * 5
# division = 10/5
# floor_divisoin = 10//3
# modulus = 10%3
# exponent = 2**3
# print(addition)
# print(subtraction)
# print(multiplication)
# print(division)
# print(floor_divisoin)
# print(modulus)
# print(exponent)

# # #concatenation
# full_name = 'john'" " + ""'doe' #johndoe
# #repetition
# repeated = 'ha'*3 #hahaha
# print(full_name, repeated)

# #strings methods
# text = "Hello World"
# print(text)
# text.lower()
# print (text.lower())
# text.upper()
# print(text.upper())
# text.strip()
# print(text.strip())
# text.replace("world","python")
# print(text.replace("world","python"))
# text.split()
# print(type(text.split()))

# # #string Formatting
# name ="esther"
# age = 25
# ajo = 2 + 6
# ola = ajo
# ajo = "ajo"
# message = f"My name is {ajo} and i'm {age} yers old"
# print(message) #My name is esther and am 25 years old 
# numbers = [1,2,3,4,5]
# print(type(numbers))

# text = ['strong', 'number','time',True, 'sign-out']
# text.append(50)
# len_text = len(text)
# text[3] = 'sign-out'
# slice = text[0:len_text -1]
# print(slice)
# print(len_text)
# print(text)

# student = {
#     'name': 'alice',
#     'age': 25,
#     'grade': 'A',
#     'course':['python','statistics']
# }
# name = student["name"]
# age = student.get("age")
# default = student.get("city","unknown")

# student["age"] = 26
# student["city"] = "new york"
# # del student["grade"]
# keys = student.keys()
# values = student.values()
# items = student.items()

# print(student['grade'])
# # print(student.keys())
# # print(student.values())
# # print(student.items())
# for key, value in student.items():
#  print(f"{key}:{value}")

# coordinates = (10,20)
# single_item = (1,)
# person = ('alice', 25, 'New York')

# x = coordinates[0]
# name, age, city = person

# print(person)

# persons = {'ate','ate','grace','grace'}
# print(persons)

# fruits = {'apple', 'banner', 'orange'}
# numbers = {1,2,3,4}
# fruits.add('grape')
# fruits.remove('banner')
# print(fruits)

# set1 = {1,2,3}
# set2 = {3,4,5}
# union = set1 | set2
# print(union)
# intersection = set1 & set2
# print(intersection)
# difference = set1 - set2
# print(difference)

# #if elif else
# age = 18
# if age < 18:
#     print("minor")
# elif age == 18:
#     print('just became an adult')
# else:
#      print('adult');


fruits = ["apple", "banana", "orange"]
for fruit in fruits:
  print(fruit)
#loop through dictionary

# def even(number):
#     remainder = number % 2
#     if remainder or 0:
#         return 'am correct'
#     else:
#         return f"this is an even number"
# message = even(40)
# print(message)

# def odd(number):
#     remainder = number % 2
#     if remainder == 5:
#         return 'am correct'
#     else:
#         return f"this is an even number"
# message = odd(5)
# print(message)

# with open('pythonnn\output.txt', 'w') as file:
#     file.write("Hello, World!\n")
#     file.writelines(["Line 1\n", "Line 2\n"])

ajo = 5
love = 5
if ajo < 5:
    print('just try')
elif ajo == love:
    print('let go')
else:
    print('get out')

def ola(text):
    # text = 'olajksjkbh'
    print(text)
    print(text)
ola('am just me')
