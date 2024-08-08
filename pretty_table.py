from prettytable import PrettyTable

table = PrettyTable()

table.field_names= ['Place', 'Team', 'Play', 'Win', 'Points'] 

teams = [
    ['Svillia', 21, 10, 35],
    ['Atletco Madred', 21, 9, 31],
    ['Real Madred', 21, 20, 51],
    ['Valencia', 21, 12, 40],
    ['FC Barcelona', 21, 15, 46],
]

# def sorted_teams(teams):
#     return teams[3]

teams.append(['Omar Madred', 21, 21, 52])

teams.sort(key= lambda team: team[3] , reverse=True)

for index, team in enumerate(teams):
    team.insert(0, index+1)
    table.add_row(team)

print(table)

