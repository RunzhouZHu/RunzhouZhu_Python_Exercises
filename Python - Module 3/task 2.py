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