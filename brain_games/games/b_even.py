from brain_games.cli import start
from random import randint


def function():
    quest_str = randint(0, 9999)
    result = 'no' if quest_str % 2 else 'yes'
    return quest_str, result


def even_start():
    start_question = 'Answer "yes" if number even otherwise answer "no".'
    start(start_question, function)
