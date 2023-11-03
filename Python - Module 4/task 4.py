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
 