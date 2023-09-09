'''
#Question 1
import random


def rollDice():
    a = random.randint(1,6)
    return a

a = 0
while a != 6:
    a = rollDice()
    print(a)

########################################
#Question 2
import random


def rollDice2(x):
    a = random.randint(1,x)
    return a

x = int(input("Please enter the sides of the dice: "))
a = 0
while a != x:
    a = rollDice2(x)
    print(a)

########################################
#Question 3
def unitConvert(x):
    y = 3.785 * x
    return y

while True:
    x = float(input("Please enter the volume in gallons: "))
    if x < 0:
        break
    y = unitConvert(x)
    print(y)
''' 
########################################
#Question 4
def sumList(x):
    sum = 0
    for a in x:
        sum = sum + a
        
    return sum

x = []
a = 0
while a >= 0:
    a = int(input("Creating list, please enter the number: "))
    x.append(a)
    
print(sumList(x))