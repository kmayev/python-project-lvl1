import prompt
import random


@property  # noqa: C901
def parity(user):

    i = 0
    YES = 'yes'
    NO = 'no'
    while i < 3:
        name, module = init()
        if (name == YES and module == 0) or \
           (name == NO and module == 1):
            print('Correct!')
            i = i + 1
        elif (name == YES and module == 1):
            prn_wrong(YES, NO)
            prn_try(user)
            break
        elif (name == NO and module == 0):
            prn_wrong(NO, YES)
            prn_try(user)
            break
        elif name != YES and name != NO:
            prn_try(user)
            break
    if i == 3:
        print('Congradulations, {}!'.format(user))


def prn_try(user):
    print('Let\'s try again, {}!'.format(user))


def prn_wrong(ans1, ans2):
    print('\'{}\' is wrong answer ;(. Correct answer was \'{}\'.')


def init():
    number = random.randint(0, 999999999999)
    print('Question: {}'.format(number))
    name = prompt.string('Your answer? ')
    module = number % 2
    return name, module
