print("Hello Ralf Pfeiffer")
print("o----")
print(" ||||")
print('*' * 10)

price = 10
rating =4.9
is_cool = True
print (price)
print(rating)
print(is_cool)

name = 'Johm Smith'
age = 20
is_new = True


# negative string index is from the end backwards
course = 'Python for Beginners'
print(course[-2])
print(course[0:3])
print(course[0: ])
print(course[2:])
#this is a string copy!
another_course = course[:]

foo='Jennifer'
print(foo[1:-1])
#'ennife'

# Formatted String
first = 'John'
last = 'Smith'
message = first+' ['+last+'] is a coder'
fmess = f'{first} [{last}] is a coder'
print(message)
print(fmess)


#len is general pupose function - also works in lists
print(len(course))

#String methods
print(course.upper())
print(course.lower())
print(course.title())
print(course)
#Ffind function returns an index
print(course.find('P'))
print(course.find('o'))
print(course.find('0')) #index is -1 if doesn't exist.
print(course.replace('Beginners', 'Absolute Newbies'))
#in operator returns A BOOLEAN
print('Python' in course)

# Arithmetic Operations
#----------------------

x=10
#Augmnted assignment operator
x+=3
print(x)
x-=5
print(x)

# Double // means the integer remainder of division
#Modulous % means the fractional remainder of division
# ** is power

#Operator Precedence
#Math Functions

x=2.9
print(round(x))
print(abs(-2.9))

import math

print(math.ceil(2.9))
print(math.floor(2.9))

#Conditions

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold:
    print("It's a cold day")
    print('Wear warm clothes')
else:
    print("It's a lovely day")
print('Enjoy your day')

good_credit = False
house_price = 1000000

if good_credit:
    downpayment = house_price * .10
else:
    downpayment = house_price * .20

print(f'Your down payment is ${str(downpayment)}')

#logical Operations
# and, or, not, >, <, >=, <=, ==, !=

name = 'Ra;lflf jfkljjkejwjpfjlkhkj'

if len(name) < 3:
    print("Name must be at least 3 chars")
elif len(name) >50:
    print('Name cannot exceed 50 characters')
else:
    print ('Name looks good')


#For Loops
sum=0
cart = [10, 20, 30, 40]
for item in cart:
    sum+=item

print(f'Sum is {sum}')

#Nested Loops

for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

#Lists

names = ['john', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)

