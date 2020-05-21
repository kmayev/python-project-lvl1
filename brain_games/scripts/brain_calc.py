#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""An example script."""
from brain_games import cli
from brain_games.games import calc


def main():

    """Run an example code."""
    cli.welcome()
    print('What is the result of the expression?')
    calc.calc(cli.welcome_user())


if __name__ == '__main__':
    main()
