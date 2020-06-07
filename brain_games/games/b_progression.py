from brain_games.cli import start
from random import randint


def function():
    start = randint(0, 9999)//100
    step = randint(0, 9999)//100
    qua = 10
    gap = randint(0, qua-1)
    return progression_generate(start, step, qua, gap)


def progression_generate(start, step, quantity, gap):
    progression_str = ''
    i = 0
    outer = 0
    for item in range(start, step * quantity + start, step):
        if i == gap:
            progression_str += '.. '
            outer = item
        else:
            progression_str += str(item) + ' '
        i += 1
    return progression_str, str(outer)


def progression_start():
    start_question = 'What number is missing in the progression?'
    start(start_question, function)
