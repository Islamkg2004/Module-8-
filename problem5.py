#  Name: Islam Syndanbekov
# Date: November 11, 2026
# Problem 5
# Check if the character has all items and no required debuffs.

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses



player1 = character('', '', '')

player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']



for item in player1.weapons:
    print("Item:", item)


for debuff in player1.weaknesses:
    print("Debuff:", debuff)



print("\nTask 1: Climb a mountain")

if ('rope' in player1.weapons and
    'coat' in player1.weapons and
    'first aid kit' in player1.weapons and
    'slow' not in player1.weaknesses):
    print("You can climb the mountain.")
else:
    print("You cannot climb the mountain.")



print("\nTask 2: Cook a meal")

if ('pan' in player1.weapons and
    'groceries' in player1.weapons and
    'small' not in player1.weaknesses):
    print("You can cook a meal.")
else:
    print("You cannot cook a meal.")



print("\nTask 3: Write a book")

if ('pen' in player1.weapons and
    'paper' in player1.weapons and
    'idea' in player1.weapons and
    'confusion' not in player1.weaknesses):
    print("You can write a book.")
else:
    print("You cannot write a book.")
