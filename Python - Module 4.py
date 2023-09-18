
#Question 1
i = 1
while i <= 1000:
    a = i % 3
    if a == 0:
        print(i)
    i = i + 1

########################################
#Question 2
inche = 0
while True:
    inche = float(input("Please enter the value of inches: "))
    if inche < 0:
        break
    print(f"{inche} inche equals to {inche * 2.54} centimeter.")

########################################
#Question 3
max = float()
min = float()
while True:
    i = input("Enter: ")
    if i == '':
        print(f"The program ends, the largest is {max}, the smallest is {min}.")
        break
    else:
        if float(i) > max:
            max = float(i)
        elif float(i) < min:
            min = float(i)        

########################################
#Question 4
import random
randomInterger = random.randint(1,10)
while True:
    answer = int(input("Please guess the number: "))
    if answer > randomInterger:
        print("Too high")
    if answer < randomInterger:
        print("Too low")
    if answer == randomInterger:
        print("Correct")
        break
  
########################################
#Question 5
times = 0
while True:
    username = input("Please enter the username: ")
    password = input("Please enter the password: ")
    if username == "python" and password == "rules":
        print("Welcome")
    else:
        print("Please try again.")
        times = times + 1
    if times == 5:
        print("Access denied")
        break

########################################
#Question 6
import random

i = 0
n = 0
N = 10000000
while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x+y*y<1:
        n = n + 1
    i = i + 1

print(4*n/N)
