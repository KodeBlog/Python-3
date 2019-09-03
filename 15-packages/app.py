from bets.pybet import name,version
import teams.english as teams
import games.champions as champs

print(f'The betting platform is {name()} and the current version is {version()}')

print(f'\nWe have the following registered teams')

for team in teams.get():
    print(team)

print(f'\nWe have the following championships')

for champ in champs.get():
    print(champ)

import os
import football_data_api
from terminaltables import AsciiTable

os.environ['FOOTBALL_DATA_API'] = "your_api_key"

data = football_data_api.CompetitionData()

competitions = data.get_available_competitions()

table_data = [
    ['Championship', 'Year']
]

for key in competitions:
    competition = [key,competitions[key]]
    table_data.append(competition)
    table = AsciiTable(table_data)

print (table.table)