from brain_games.logic import cli
import random


# @property  # noqa: C901
def calc(user, si):

    i = 0
    while i < 3:
        if si == 'CALC':
            a1, a2 = cli.cli_random(), cli.cli_random()
            oper = cli.rand_s()
            quest_str = str(a1) + oper + str(a2)
            result = do_it(a1, a2, oper)
        elif si == 'NOD':
            a1, a2 = cli.cli_random(), cli.cli_random()
            quest_str = str(a1) + ' ' + str(a2)
            result = nod(a1, a2)
        elif si == 'PRO':
            start = cli.cli_random()//100
            step = cli.cli_random()//100
            qua = 10
            gap = random.randint(0, qua-1)
            result, quest_str = progression_generate(start, step, qua, gap)
        answer = cli.prn_question(quest_str)
        if not answer.isdigit() or int(answer) != result:
            cli.prn_wrong(answer, result)
            cli.prn_try(user)
            return
        else:
            cli.prn_correct()
            i += 1
    cli.prn_winner(user)


def do_it(a1, a2, si):
    if si == '+':
        return a1 + a2
    elif si == '-':
        return a1 - a2
    elif si == '*':
        return a1 * a2


def nod(a1, a2):
    while a1 != 0 and a2 != 0:
        if a1 > a2:
            a1 %= a2
        else:
            a2 %= a1
    return a1 + a2


def progression_generate(start, step, quantity, gap):
    prog = ''
    i = 0
    outer = 0
    for iter in range(start, step * quantity + start, step):
        if i == gap:
            prog += '.. '
            outer = iter
        else:
            prog += str(iter) + ' '
        i += 1
    return outer, prog
