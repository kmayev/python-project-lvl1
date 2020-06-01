from brain_games.logic import cli
from brain_games.logic import parity
from brain_games.logic import calc


# n_of_game = 1 - brain-games
# n_of_game = 2 - brain-even
# n_of_game = 3 - brain-calc
# n_of_game = 4 - brain-gcd
# n_of_game = 5 - brain-prime
# n_of_game = 6 - brain-progression

def start(n_of_game, title):
    cli.welcome()
    print(title, end='\n\n')
    u_name = cli.welcome_user()
    if n_of_game == 2: 					# even
        parity.parity(u_name, 'EVEN')
    elif n_of_game == 3: 					# calc
        calc.calc(u_name, 'CALC')
    elif n_of_game == 4: 					# gcd
        calc.calc(u_name, 'NOD')
    elif n_of_game == 5: 					# prime
        parity.parity(u_name, 'PRIME')
    elif n_of_game == 6: 					# progression
        calc.calc(u_name, 'PRO')
