from brain_games import engine
from brain_games import cli


def function():
    a1 = cli.cli_random()
    a2 = cli.cli_random()
    oper = cli.rand_s()
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
    engine.start(start_question, function)
