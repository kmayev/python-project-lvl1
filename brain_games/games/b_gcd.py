from brain_games.cli import start
from random import randint


def prepare_data():
    a1, a2 = randint(0, 9999), randint(0, 9999)
    question = str(a1) + ' ' + str(a2)
    result = calculate_gcd(a1, a2)
    return question, str(result)


def calculate_gcd(a1, a2):
    while a1 != 0 and a2 != 0:
        if a1 > a2:
            a1 %= a2
        else:
            a2 %= a1
    return a1 + a2


def start_gcd():
    start_question = 'Find the greatest common divisor of given numbers.'
    start(start_question, prepare_data)
