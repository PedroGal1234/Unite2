#Pedro Gallino
#9/25/17
#quiz2/py - my seond proggramming quiz on if statements

num1 = float(input('Enter Number 1: '))
num2 = float(input('Enter Number 2: '))

if num2 == num1:
    print('Your numbers are the same')
elif num2>num1:
    print('The second number is bigger')
elif num2<num1:
    print('the first number is bigger')

if num1%3 == 0 and num2%3 == 0:
    print('Both of your numbers are divisible by three')
elif num1%3 == 0:
    print('Only the first number is divisible by three')
elif num2%3 == 0:
    print('Only the second number is divisible by three')
else:
    print('None of your numbers are divisible by three')

product = float(input('Enter the product of your two numbers: '))

if product == (num1*num2):
    print('Correct')
else:
    print('Worng')