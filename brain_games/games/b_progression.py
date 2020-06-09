from brain_games.cli import start
from random import randint


def progression_data_prepare():
    start = randint(0, 9999)//100
    step = randint(0, 9999)//100
    quantity_of_numbers = 10
    gap = randint(0, quantity_of_numbers - 1)
    return progression_with_gap_generate(start, step, quantity_of_numbers, gap)


def progression_with_gap_generate(start, step, quantity, gap):
    progression_str = ''
    i = 0
    missed = ''
    for item in range(start, step * quantity + start, step):
        if i == gap:
            progression_str += '.. '
            missed = str(item)
        else:
            progression_str += str(item) + ' '
        i += 1
    return progression_str.strip(), missed


def progression_start():
    start_question = 'What number is missing in the progression?'
    start(start_question, progression_data_prepare)
