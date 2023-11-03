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