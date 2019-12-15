import csv
import os
from urllib.request import urlretrieve
from collections import defaultdict

BATTLE_DATA = os.path.join('/tmp', 'battle-table.csv')
if not os.path.isfile(BATTLE_DATA):
    urlretrieve('https://bit.ly/2U3oHft', BATTLE_DATA)


def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    result = defaultdict(dict)
    with open(BATTLE_DATA) as b:
        reader = csv.DictReader(b)
        for row in reader:
            result[row['Attacker']] = row
    return result


def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()
    if player1 not in defeat_mapping or player2 not in defeat_mapping:
        raise ValueError()
    return {'win': player1,
            'lose': player2,
            'draw': 'Tie'}[defeat_mapping[player1][player2]]
