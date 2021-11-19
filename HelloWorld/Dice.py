import random


class Dice:
    def roll(self):
        onepl = random.randint(1,6)
        twopl = random.randint(1,6)
        return onepl, twopl

dice = Dice()
print(dice.roll())



