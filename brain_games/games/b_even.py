from brain_games import engine
from brain_games import cli


def function():
    quest_str = cli.cli_random()
    result = 'no' if quest_str % 2 else 'yes'
    return quest_str, result


def even_start():
    start_question = 'Answer "yes" if number even otherwise answer "no".'
    engine.start(start_question, function)
