# https://goheels.com/sports/mens-basketball/roster
import pandas as pd

# Creating a dictionary for the players with the required data
players = {
    "Last Name": ["Tyson", "Davis", "Cadeau", "Claude", "Brown", "Davis", "Trimble", "Powell", "Jackson", "Washington"],
    "First Name": ["Cade", "RJ", "Elliot", "Tyzhaun", "James", "Elijah", "Seth", "Drake", "Ian", "Jalen"],
    "Height (in)": [79, 72, 73, 79, 82, 75, 75, 78, 76, 82],
    "Weight (lbs)": [200, 180, 180, 230, 215, 215, 195, 195, 190, 235]
}

data = pd.DataFrame(players)

# Calculate BMI and round it to 2 decimal points
data["BMI"] = ((data["Weight (lbs)"] / 2.205) / ((data["Height (in)"] / 39.37) ** 2)).round(2)

# Print the DataFrame
print(data)




