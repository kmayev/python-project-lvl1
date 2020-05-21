#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""An example script."""
from brain_games import cli
from brain_games.games import parity


def main():

    """Run an example code."""
    cli.welcome()
    print('Answer "yes" if number even otherwise answer "no".')
    parity.parity(cli.welcome_user())


if __name__ == '__main__':
    main()
