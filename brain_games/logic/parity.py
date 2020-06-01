from brain_games.logic import cli


def parity(user, type):

    i = 0
    YES = 'yes'
    NO = 'no'
    while i < 3:
        number = cli.cli_random()
        answer = cli.prn_question(number)
        module = choice(type,  number)

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


def isprime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def choice(type, number):
    if type == 'EVEN':
        return number % 2
    elif type == 'PRIME':
        return 0 if isprime(number) else 1
