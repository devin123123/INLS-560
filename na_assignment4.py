# Constants Sales Manager Position
MIN_YEARS_BAKING = 3
CAKES_MADE = 10

years_baking = int(input('Enter your years of baking experience:'))
cakes_made = int(input('Enter how many cakes you have made this year:'))

if years_baking >= MIN_YEARS_BAKING and cakes_made >= CAKES_MADE:
    print('Congratulation! You are eligible for the Head Baker Position.')
else:
    # Multi-line with f-string
    print(f'''
          
Sorry, you do not meet the requirements for the Head Baker Position

You need at least:
- {MIN_YEARS_BAKING} years of baking experience
- {CAKES_MADE} cakes made this year ''')