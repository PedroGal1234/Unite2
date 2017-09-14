#Pedro Gallino
#9/14/17
#fortuneTeller.py - tells a fortune

color = (input('Pick a color red or blue: '))
num = int(input('Pick a number from 1-4: '))

if color == 'red' and num == 1:
    print('You will live to be 200 years old')
elif color == 'red' and num == 2:
    print('You will survive a mountain lion attack')
elif color == 'red' and num == 3:
    print('You will meet the most annoying person ever: Clay')
elif color == 'red' and num == 4:
    print('You will find a bear in your bedroom today')
elif color == 'blue' and num == 1:
    print('You will win the powerball')
elif color == 'blue' and num == 2:
    print('you will loose 100,000 dollars tomorrow')
elif color == 'blue' and num == 3:
    print('You will crash your car and loose an eye')
elif color == 'blue' and num == 4:
    print('you will find an iphone X on the ground two years from now')
else:
    print("This doesn't work")