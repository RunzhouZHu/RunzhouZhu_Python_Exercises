#Question 1
lengthOfZander =  float(input("Please enter the length of zander in centimeter: "))
if lengthOfZander < 42:
    print(f"Please release the fish back into the lack.")
    print(f"the fish your caught is {42 - lengthOfZander} centimeters below the size limit.")
########################################
 
#Question 2
print("The cabin classes are LUX, A, B and C.")
cabinClass = input("Please enter your cabin class of a cruise ship.")
if cabinClass == 'LUX':
    print("upper-deck cabin with a balcony.")
elif cabinClass == 'A':
    print("above the car deck, equipped with a window.")
elif cabinClass == 'B':
    print("windowless cabin above the car deck.")
elif cabinClass == 'C':
    print("windowless cabin below the car deck.")
else:
    print("Error! Invalid cabin class.") 
########################################

#Question 3
biologicalGender = input("Please enter your biological gender(enter f or m): ")
if biologicalGender == 'f':
    highValue = 155
    lowValue = 117
elif biologicalGender == 'm':
    highValue = 167
    lowValue = 134

hemoglobinValue = float(input("Please enter your hemoglobin value (g/l): "))
if hemoglobinValue < lowValue:
    print("Your hemoglobin value is low.")
elif hemoglobinValue >= lowValue and hemoglobinValue <= highValue:
    print("Your hemoglobin value is normal.")
elif hemoglobinValue > highValue:
    print("Your hemoglobin value is high.")
########################################
#Queston 4
year = int(input("Please enter the year."))
if year%100 == 0:
    if year % 400 == 0:
        print("This year is a leap year.")
    else:
        print("This year is not a leap year.")
elif year%4 == 0:
    print("This year is a leap year.")    
else:
    print("This year is not a leap year.")   