#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""An example script."""
from brain_games import cli
from brain_games.games import calc


def main():

    """Run an example code."""
    cli.welcome()
    print('Find the greatest common divisor of given numbers.', end = '\n\n')
    calc.calc(cli.welcome_user(), 2)


if __name__ == '__main__':
    main()
