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