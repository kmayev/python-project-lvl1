from brain_games.cli import start
from random import randint


def prepare_data():
    QUANTITY = 10
    first = randint(0, 9999)//100
    step = randint(0, 9999)//100
    missed = first + step * randint(0, QUANTITY - 1)
    sequence = range(first, step * QUANTITY + first, step)
    return make_question(sequence, missed), str(missed)


def make_question(sequence, missed):
    return ' '.join(map(lambda x: '..' if x == missed else str(x), sequence))


def start_progression():
    start_question = 'What number is missing in the progression?'
    start(start_question, prepare_data)
