#Pedro Gallino
#9/14/17
#unitConverter.py - converts units

print('1)Kilometers to Miles')
print('2)Kilograms to Pounds')
print('3)Liters to Gallons')
print('4)Celsius to Fahrenheit')
rate = int(input('Choose a Number:'))

if rate==1:
    km = float(input('Enter number of kilometers:'))
    print(km,'Kilometers is',km*0.621371,'miles')
elif rate==2:
    kg = float(input('Enter number of kilograms:'))
    print(kg,'Kilograms is',kg*2.20462,'pounds')
elif rate==3:
    liter = float(input('Enter number of Liters:'))
    print(liter,'Liter is',liter*0.264172,'Gallons')
elif rate==4:
    cel = float(input('Enter degrees Celsius:'))
    print(cel,'degrees Celsius is',(cel*(9/5))+32,'degrees Fahrenheit')


