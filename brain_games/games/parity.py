from brain_games import cli


# @property  # noqa: C901
def parity(user):

    i = 0
    YES = 'yes'
    NO = 'no'
    while i < 3:
        number = cli.cli_random()
        answer = cli.prn_question(number)
        module = number % 2
        if (answer == YES and module == 1):
            cli.prn_wrong(YES, NO)
            cli.prn_try(user)
            return
        elif (answer == NO and module == 0):
            cli.prn_wrong(NO, YES)
            cli.prn_try(user)
            return
        elif answer != YES and answer != NO:
            cli.prn_try(user)
            return
        elif (answer == YES and module == 0) or \
             (answer == NO and module == 1):
            cli.prn_correct()
            i += 1

    cli.prn_winner(user)
