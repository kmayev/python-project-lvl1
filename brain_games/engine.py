from brain_games import cli


def start(title, function):
    cli.welcome()
    print(title, end='\n\n')
    u_name = cli.welcome_user()
    if function is None:
        return
    i = 0
    while i < 3:
        quest_str, result = function()
        answer = cli.prn_question(quest_str)
        if answer != result:
            cli.prn_wrong(answer, result)
            cli.prn_try(u_name)
            return
        else:
            cli.prn_correct()
            i += 1
    cli.prn_winner(u_name)
