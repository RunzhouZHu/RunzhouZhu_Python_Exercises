import random


diceRoll = []
n = int(input("Please enter the number of dices :"))
i = 0
sum = 0
while i < n:
    diceRoll.append(random.randint(1,6))
    i = i + 1
    
for x in diceRoll:
    sum = sum + x
    
print(sum)