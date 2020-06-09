from brain_games.cli import start
from random import randint


def gcd_data_prepare():
    a1, a2 = randint(0, 9999), randint(0, 9999)
    quest_str = str(a1) + ' ' + str(a2)
    result = gcd_calculate(a1, a2)
    return quest_str, str(result)


def gcd_calculate(a1, a2):
    while a1 != 0 and a2 != 0:
        if a1 > a2:
            a1 %= a2
        else:
            a2 %= a1
    return a1 + a2


def gcd_start():
    start_question = 'Find the greatest common divisor of given numbers.'
    start(start_question, gcd_data_prepare)
