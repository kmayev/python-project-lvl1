from brain_games.cli import start
from random import randint


def prime_data_prepare():
    quest_str = randint(0, 9999)
    result = 'yes' if is_prime(quest_str) else 'no'
    return quest_str, result


def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def prime_start():
    start_question = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'
    start(start_question, prime_data_prepare)
