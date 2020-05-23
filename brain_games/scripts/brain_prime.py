#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""An example script."""
from brain_games import cli
from brain_games.games import parity


def main():

    """Run an example code."""
    cli.welcome()
    print('Answer "yes" if given number is prime. Otherwise answer "no".',
          end='\n\n')
    parity.parity(cli.welcome_user(), 'PRIME')


if __name__ == '__main__':
    main()
