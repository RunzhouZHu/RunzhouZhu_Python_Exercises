import random


def rollDice():
    a = random.randint(1,6)
    return a

a = 0
while a != 6:
    a = rollDice()
    print(a)