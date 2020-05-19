#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""An example script."""
from brain_games import cli
from brain_games import parity


def main():
    """Run an example code."""
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    uname = cli.welcome_user()
    parity.parity(uname)

if __name__ == '__main__':
    main()
