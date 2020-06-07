from brain_games.cli import start
from random import randint,  choice


def function():
    a1 = randint(0, 9999)
    a2 = randint(0, 9999)
    oper = choice(['+', '-', '*'])
    quest_str = str(a1) + oper + str(a2)
    if oper == '+':
        result = a1 + a2
    elif oper == '-':
        result = a1 - a2
    elif oper == '*':
        result = a1 * a2
    return quest_str, str(result)


def calc_start():
    start_question = 'What is the result of the expression?'
    start(start_question, function)
