from brain_games import cli


# @property  # noqa: C901
def calc(user, si):

    i = 0
    while i < 3:
        a1 = cli.cli_random()
        a2 = cli.cli_random()
        if si == 1:
            oper = cli.rand_s()
        elif si == 2:
            oper = ' '
        result = do_it(a1, a2, oper)
        quest_str = str(a1) + oper + str(a2)
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
    elif si == ' ':
        return nod(a1, a2)


def nod(a1, a2):
    while a1 != 0 and a2 != 0:
        if a1 > a2:
            a1 %= a2
        else:
            a2 %= a1
    return a1 + a2
