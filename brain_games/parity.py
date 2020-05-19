import prompt
import random


def parity(user):
    i=0
    while i < 3:
        number = random.randint(0, 999999999999)
        print('Question: {}'.format(number))  
        name = prompt.string('Your answer? ')
        if (name == 'yes' and number%2 == 0) or (name == 'no' and number%2 == 1):
            print('Correct!')
            i =  i + 1
        elif (name == 'yes' and number%2 == 1):
            print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
            print('Let\'s try again, {}!'.format(user))
            break
        elif (name == 'no' and number%2 == 0):
            print('\'no\' is wrong answer ;(. Correct answer was \'yes\'.')
            print('Let\'s try again, {}!'.format(user))
            break
        elif name != 'yes' and name != 'no':
            print('Let\'s try again, {}!'.format(user))
            break
    if i == 3:
        print('Congradulations, {}!'.format(user))    	
