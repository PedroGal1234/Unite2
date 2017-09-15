#Pedro Gallin
#9/15/17
#adventure.py - tells oyu an adventure

print('Always answer yes or no')
answer1 = input('Your are in the middle of the woods and there is a water fall do you go explore? ')
if answer1 == 'yes':
    answer2 = input('You sprint over and there is a tiger, do you run? ')
    if answer2 == 'yes':
        print('You start running but the tiger is catching up')
        answer3 = input('You see a tall tree, do you try to climb it? ')
        if answer3 == 'yes':
            print('There are no low branches and the tiger catches up and eats you')
        elif answer3 == 'no':
            print('You run and meet a hunter who shoots the tiger in the head, you live and you made a new friend')
    if answer2 == 'no':
        print('You punch the tiger in the head, and start fighting it')
        answer4 = input('The tiger bites your arm, do you try to run? ')
        if answer4 == 'yes':
            print('You try and run but the tiger bits your face off')
        if answer4 == 'no':
            print('You pick up a rock and kill the tiger, then you find a house and the person inside takes care of you')
if answer1 == 'no':
    answer5 = input('After more walking you find a cave do you go explore? ')
    if answer5 == 'yes':
        answer6 = input('You here a scream do you continue going into the cave? ')
        if answer6 == 'yes':
            print('You find a swarm of bats and they attack and kill you')
        elif answer6 == 'no':
            print('You turn around but a hunter thinks you are a deer and shoots you in the heart')
    if answer5 == 'no':
        answer7 = input('You turn around and find a bear, do you run? ')
        if answer7 == 'yes':
            print("You aren't fast enough and the tiger kills you")
        if answer7 == 'no':
            print("You try and fight the bear but he knocks you down and kills you")