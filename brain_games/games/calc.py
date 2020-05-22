from brain_games import cli
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
            shag = cli.cli_random()//100
            kolvo = 10
            dirka = random.randint(0, kolvo-1)
            result, quest_str = prog(start, shag, kolvo, dirka)
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
        return a1 + a2, None
    elif si == '-':
        return a1 - a2, None
    elif si == '*':
        return a1 * a2, None


def nod(a1, a2):
    while a1 != 0 and a2 != 0:
        if a1 > a2:
            a1 %= a2
        else:
            a2 %= a1
    return a1 + a2


def prog(start, shag, kolvo, dirka):
    prog = ''
    i = 0
    outer = 0
    for iter in range(start, shag * kolvo + start, shag):
        if i == dirka:
            prog += '.. '
            outer = iter
        else:
            prog += str(iter) + ' '
        i += 1
    return outer, prog
