from brain_games import cli


# @property  # noqa: C901
def calc(user):

    i = 0
#    YES = 'yes'
#    NO = 'no'
    while i < 3:
        a1 = cli.cli_random()
        a2 = cli.cli_random()
        si = cli.rand_s()
        result = do_it(a1, a2, si)
        quest_str = str(a1) + si + str(a2)
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
