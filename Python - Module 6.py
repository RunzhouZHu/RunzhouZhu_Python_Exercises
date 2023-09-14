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

########################################
#Question 4
def sumOfList(lst):
    return sum(lst)

lst = [1, 2, 3, 4, 5]
total = sumOfList(lst)
print("The sum of the list is:", total)

########################################
#Question 5
def removeOddNumbers(lst):
    
    return [num for num in lst if num % 2 == 0]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original list:", lst)
even_lst = removeOddNumbers(lst)
print("List with odd numbers removed:", even_lst)
'''
########################################
#Question 6
def pizzaCalculator(diameter, price):
    unitPrice = price/(3.14*(diameter/2)**2)
    return unitPrice

diameter1 = float(input("Please enter the diameter of first pizza: "))
price1 = float(input("Please enter the price of first pizza: "))
diameter2 = float(input("Please enter the diameter of second pizza: "))
price2 = float(input("Please enter the price of second pizza: "))

unitPrice1 = pizzaCalculator(diameter1,price1)
unitPrice2 = pizzaCalculator(diameter2,price2)

if unitPrice1 > unitPrice2:
    print("The first pizza provides better value for money.")
elif unitPrice1 < unitPrice2:
    print("The second pizza provides better value for money.")
elif unitPrice1 == unitPrice2:
    print("The two pizza provides the same value for money.")