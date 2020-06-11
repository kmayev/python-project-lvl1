from brain_games.cli import start
from random import randint


def prepare_data():
    question = randint(0, 9999)
    result = 'no' if question % 2 else 'yes'
    return question, result


def start_even():
    start_question = 'Answer "yes" if number even otherwise answer "no".'
    start(start_question, prepare_data)
