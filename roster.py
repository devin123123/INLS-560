# https://goheels.com/sports/mens-basketball/roster
import pandas as pd
roster = ['Tyson', 'Davis', 'Cadeau']
player = {"Last Name": roster,
          "First Name": ["Cade", "RJ", "Elliot"], 
          "height": [79, 72, 73], 
          "weight": [200,180,180]}
data = pd.DataFrame(player)
print(data)



