import pandas as pd

races = pd.read_csv('races.csv')
drivers = pd.read_csv('drivers.csv')

out = open('nascar.txt', 'w')

names = list(drivers['x'])
for race in races.iterrows():
    race_names = list(map(lambda x: names[x-1], race[1].values))
    out.write(','.join(race_names) + '\n')
