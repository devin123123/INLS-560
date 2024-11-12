# https://goheels.com/sports/mens-basketball/roster
import pandas as pd

roster = ['Tyson', 'Davis', 'Cadeau']

data = pd.DataFrame(roster, columns=['Last Name'])
print(data)


