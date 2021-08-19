name = input('Please enter your name')
print('Hello', name)

num1 = input('Enter num1')
num2 = input('Enter num2')
if num1.isdigit() and num2.isdigit():
    print(int(num1) + int(num2))

# else:
    print('Invalid enter')

import datetime
name = input('Enter your name')
age = input('Enter your age')

today = datetime.date.today()
print(today.year)
if age.isdigit():
    print('Hello', name, 'You will be 100 in', today.year + (100-int(age)))

num = input('Enter number')

if int(num) > 0:
    if int(num) % 2 == 0:
        print ('Yes')
    else:
        print('No')
else:
    print('Not valid input')

num = input ('Enter number')

if int(num) > 0:
    print(int(num) + int(num)**2 + int(num)**3)

import random

x = random.randint(1,2)
print(x)
