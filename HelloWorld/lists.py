
#Lists

#Largest Number

numbers = [8, 3, 7,4, 9, 11, 2, 1]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest=num

print(f' Largest={largest}')

#2D Lists

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][1])
matrix[0][1] = 20
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)
#List methods

print(numbers)
numbers.append(20)
print(numbers)
numbers.insert(0, 15)
print(numbers)
numbers.remove(20)
print(numbers)
print(numbers.index(7))
print(11 in numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

#add more duplicates
numbers.append(7)
numbers.insert(0,7)

numbers.append(12)
numbers.insert(0,12)

numbers.append(5)
numbers.insert(0,5)

#numbers.pop()

#numbers.index(11)
#



num2 = numbers.copy()
#remove duplicates - rips algorithm
print(f'duplicate numbers={numbers}')
for item in numbers:
    print(f'[{item}]')
    for i in range(numbers.count(item)):
        if i>0:
            numbers.remove(item)
print(f'unique numbers={numbers}')

uniques = []

for num in num2:
    if num not in uniques:
        uniques.append(num)

print(uniques)

#Tuples

#immutable lists - use parens
numbers = (1,2,3)

#Can only use function that read Tuples

#Unpacking for Lists and Tuples

coordinates = (1,2,3)
x=coordinates[0]
y=coordinates[1]
z=coordinates[2]

#this is same as above...
x,y,z = coordinates

#DICTIONARIES

customer = {
    'name': 'John Smith',
    'age': 30,
    'is_verified': True
}

#Will cause error
#customer["Name"]

# so use get - will return None
print(customer.get("birthdate"))
print(customer.get("birthdate", "Jan 1 1980"))
customer["birthdate"] = "01011980"
print(customer.get("birthdate", "Jan 1 1980"))

#NUmbers

nums = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '0': 'Zero'
}

phone_no = input ('Phone: ')

out=''
for digit in phone_no:
    out += nums.get(digit, '!')+" "
print(out)

#Emoji Converter
# Functions

def emoji_converter(message):
    tokens = message.split(' ')
    emojis = {
    ':)': '😀',
    ':(': '🙁'
    }

    output = ""
    for token in tokens:
        output += emojis.get(token, token) + ' '
    return output


message = input(">")
print(emoji_converter(message))


#Parameters
def greet_user(first_name, last_name):
    print (f'Hi {first_name}, {last_name}')
    print ('Welcome Aboard!')

#using positional parameters
greet_user('Mary', 'blige')
#using keyword arguments - if mixed keyword args should be after positional args
greet_user(last_name='Smith', first_name='John')

#return statement

def square(num):
    return num * num


print(square(4))

#Exceptions

try:
    age = int(input('Age: '))
    income = 20000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('InvalidValue')


#modules
from utils import find_max

numbers = [10,3,6,9,2,11,5,7]
print(find_max(numbers))










