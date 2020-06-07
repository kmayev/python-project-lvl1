from brain_games.cli import start
from random import randint


def function():
    quest_str = randint(0, 9999)
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
    start(start_question, function)
