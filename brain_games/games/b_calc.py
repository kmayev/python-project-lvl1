from brain_games.cli import start
from random import randint,  choice
from operator import add, mul, sub


def calc_data_prepare():
    a1 = randint(0, 9999)
    a2 = randint(0, 9999)
    oper = choice(['+', '-', '*'])
    quest_str = str(a1) + oper + str(a2)
    if oper == '+':
        result = add(a1, a2)
    elif oper == '-':
        result = sub(a1, a2)
    elif oper == '*':
        result = mul(a1, a2)
    return quest_str, str(result)


def calc_start():
    start_question = 'What is the result of the expression?'
    start(start_question, calc_data_prepare)
