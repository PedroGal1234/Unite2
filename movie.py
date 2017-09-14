#Pedro Gallino
#9/14/17
#movie.py - tells you what rated movie you can watch

age = int(input('Enter your age: '))

if age<13:
    print('You can watch G and PG movies')
elif age<17:
     print('You can watch PG-13 movies')
elif age<18:
     print('You can watch NC-17 movies')
else:
    print('You can watch any movies')
    
