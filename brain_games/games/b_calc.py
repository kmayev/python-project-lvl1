from brain_games.cli import start
from random import randint,  choice
from operator import add, mul, sub


def prepare_data():
    a1 = randint(0, 9999)
    a2 = randint(0, 9999)
    oper = choice(['+', '-', '*'])
    question = str(a1) + oper + str(a2)
    if oper == '+':
        result = add(a1, a2)
    elif oper == '-':
        result = sub(a1, a2)
    elif oper == '*':
        result = mul(a1, a2)
    return question, str(result)


def start_calc():
    start_question = 'What is the result of the expression?'
    start(start_question, prepare_data)
