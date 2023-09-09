'''
#Question 1
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

########################################
#Question 2
numbers = []
while True:
    n = input("Please enter a number: ")
    if n == '':
        break
    numbers.append(n)
    
i = 0
numbers.sort(reverse=True)
while i < 5:
    print(numbers[i])
    i = i + 1
'''
########################################
#Question 3
integer = int(input("Please enter a interger: "))
i = 1
while i < integer:
    i = i + 1
    if integer % i == 0:
        print("This is not a prime number.")
        break
    else:
        print("This is a prime number.")
        break
    
########################################
#Question 4
