# https://goheels.com/sports/mens-basketball/roster
import pandas as pd

player = {"Last Name": ["Tyson", "Davis", "Cadeau"],
          "First Name": ["Cade", "RJ", "Elliot"], 
          "height": [79, 72, 73], 
          "weight": [200,180,180]}
data = pd.DataFrame(player)
print(data)



