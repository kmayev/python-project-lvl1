import prompt


def start(title, prepare_data_function):
    print('Welcome to the Brain Games!\n{}'.format(title), end='\n\n')
    u_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(u_name), end='\n\n')
    NUMBER_OF_ATTEMPTS = 3
    i = 0
    while i < NUMBER_OF_ATTEMPTS:
        question, result = prepare_data_function()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer? ')
        if answer != result:
            print("'{}' is wrong answer ;(. Correct answer was '{}'\n".
                  format(answer, result))
            print("Let's try again, {}!".format(u_name))
            return
        else:
            print('Correct!')
            i += 1
    print('Congradulations, {}!'.format(u_name))
