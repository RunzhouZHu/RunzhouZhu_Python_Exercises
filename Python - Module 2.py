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
sum = num1 + num2 + num3
product = num1 * num2 * num3
average = sum / 3
print(f"The ")