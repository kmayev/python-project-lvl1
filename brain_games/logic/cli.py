import prompt
import random


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name), end='\n\n')
    return name


def welcome():
    print('Welcome to the Brain Games!')


def prn_winner(user):
    print('Congradulations, {}!'.format(user))


def prn_try(user):
    print('Let\'s try again, {}!'.format(user))


def prn_wrong(ans1, ans2):
    print('\'{0}\' is wrong answer ;(. Correct answer was \'{1}\'.'
          .format(ans1, ans2))


def prn_correct():
    print('Correct!')


def prn_question(question):
    print('Question: {}'.format(question))
    return prompt.string('Your answer? ')


def cli_random():
    return random.randint(0, 9999)


def rand_s():
    return random.choice(['+', '-', '*'])
