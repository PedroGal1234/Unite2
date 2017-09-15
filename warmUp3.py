#Pedro Gallin
#9/15/17
#warmUp3.py- sees if a number is divisible by 2 or three

num = int(input('Enter a number: '))

if num%2 == 0 and num%3 == 0:
    print(num,'Is divisible by 3 and 2')
elif num%2 == 0:
    print(num,'Is divisible by 2')
elif num%3 == 0:
    print(num,'is diviseble by 3')
else:
    print(num,'Is not divisible by 2 or 3')
