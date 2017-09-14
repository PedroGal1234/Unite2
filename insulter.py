#Pedro Gallino
#9/14/17
#insulter.py- insults people

from random import randint

name = input('What is your name: ')
num = randint(1,5)

if num == 1:
    print('If you look up',name,'In the dictionary, it says the sutpidest: person ever')
elif num == 2:
    print('You are a potato')
elif num == 3:
    print('Your feet smell')
elif num == 4:
    print('You have no friends')
elif num == 5:
    print('People like you (sarcasm)')