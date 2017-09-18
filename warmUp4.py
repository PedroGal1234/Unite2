#Pedro Gallino
#9/18/17
#warmUp4.py - asks user for a number and prints the number or buzz

num = int(input('Enter a number: '))

if '7' in str(num) or num%7 == 0:
     print('Buzz')
else:
    print(num)
