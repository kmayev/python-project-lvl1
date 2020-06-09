import prompt


def start(title, function):
    print('Welcome to the Brain Games!\n'+title, end='\n\n')
    u_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(u_name), end='\n\n')
    NUMBER_OF_ATTEMPTS = 3
    i = 0
    while i < NUMBER_OF_ATTEMPTS:
        quest_str, result = function()
        print('Question: {}'.format(quest_str))
        answer = prompt.string('Your answer? ')
        if answer != result:
            print('\'{0}\' is wrong answer ;(. Correct answer \
was \'{1}\'\nLet\'s try again, {2}!' .format(answer, result, u_name))
            return
        else:
            print('Correct!')
            i += 1
    print('Congradulations, {}!'.format(u_name))
