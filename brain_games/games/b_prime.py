from brain_games import engine
from brain_games import cli


def function():
    quest_str = cli.cli_random()
    result = 'yes' if isprime(quest_str) else 'no'
    return quest_str, result


def isprime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def prime_start():
    start_question = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'
    engine.start(start_question, function)
