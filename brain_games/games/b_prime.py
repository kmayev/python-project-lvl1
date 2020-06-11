from brain_games.cli import start
from random import randint


def prepare_data():
    question = randint(0, 9999)
    result = 'yes' if is_prime(question) else 'no'
    return question, result


def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def start_prime():
    start_question = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'
    start(start_question, prepare_data)
