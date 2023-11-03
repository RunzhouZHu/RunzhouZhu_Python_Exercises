import random


def rollDice2(x):
    a = random.randint(1,x)
    return a

x = int(input("Please enter the sides of the dice: "))
a = 0
while a != x:
    a = rollDice2(x)
    print(a)