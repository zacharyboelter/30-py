# for x in range(5):
#     print(x)

# for i in range(50):
#     print(i)


# nested loop to print every dominoe with no doubles

for left in range(7):
    for right in range(left, 7):
        print(f'[{left} | {right}]', end=' ')
    print()


teams = ['pandas', 'dragons', 'rats', 'snakes', 'clippers', 'sharks']

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(f"Home: {home_team.capitalize()} vs Away: {away_team.capitalize()}")