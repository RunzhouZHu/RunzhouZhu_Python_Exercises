# Question 1
name = input("Please enter your name: ")
print("Hello, " + name + "!")
########################################
# Question 2
import math
radius = float(input("Please enter the radius of circle: "))
areaOfCircle = math.pi * radius * radius
print(f"The area of the circle is {areaOfCircle}.")
########################################
# Question 3
lengthOfRectangle = float(input("Please enter the length of rectangle: "))
widthOfRectangle = float(input("Please enter the width of rectangle: "))
perimeterOfRectangle = 2 * lengthOfRectangle + 2 * widthOfRectangle
areaOfRectangle = lengthOfRectangle * widthOfRectangle
print(f"The perimeter of the rectangle is {perimeterOfRectangle}.")
print(f"The area of the rectangle is {areaOfRectangle}.")
########################################
# Question 4
num1 = int(input("Please enter the 1st number: "))
num2 = int(input("Please enter the 2nd number: "))
num3 = int(input("Please enter the 3rd number: "))
Sum = num1 + num2 + num3
product = num1 * num2 * num3
average = Sum / 3
print(f"The sum of the numbers is {Sum}.")
print(f"The product of the numbers is {product}.")
print(f"The average of the numbers is {average}.")
########################################
# Question 5
talents = float(input("Enter talents: \n\n"))
pounds = float(input("Enter pounds: \n\n"))
lots = float(input("Enter lots: \n\n"))

g = 13.3 * (32 * (20 * talents + pounds) + lots)
kilograms = int(g / 1000)
grams = round(g - 1000 * kilograms, 2)

print(f"The weight in modern units:\n{kilograms} kilograms and {grams} grams.")
########################################
# Question 6
import random

code1digit1 = str(random.randint(0, 9))
code1digit2 = str(random.randint(0, 9))
code1digit3 = str(random.randint(0, 9))
print(f"The 3-digit code is {code1digit1 + code1digit2 + code1digit3}")

code2digit1 = str(random.randint(1, 6))
code2digit2 = str(random.randint(1, 6))
code2digit3 = str(random.randint(1, 6))
code2digit4 = str(random.randint(1, 6))
print(f"The 3-digit code is {code2digit1 + code2digit2 + code2digit3 + code2digit4}")