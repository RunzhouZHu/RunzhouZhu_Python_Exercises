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

########################################
#Question 3
n = int(input("Please enter a interger: "))
for x in range(2,n-1):
    if n % x == 0:
        print("This is not a prime number.")
        break
    else:
        print("This is a prime number.")
        break

########################################
#Question 4
cityNames = []
for x in range(5):
    x = input("Please enter the name: ")
    cityNames.append(x)
    
for y in cityNames:
    print(y)