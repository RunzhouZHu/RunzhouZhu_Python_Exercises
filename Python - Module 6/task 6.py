def pizzaCalculator(diameter, price):
    unitPrice = price/(3.14*(diameter/2)**2)
    return unitPrice

diameter1 = float(input("Please enter the diameter of first pizza: "))
price1 = float(input("Please enter the price of first pizza: "))
diameter2 = float(input("Please enter the diameter of second pizza: "))
price2 = float(input("Please enter the price of second pizza: "))

unitPrice1 = pizzaCalculator(diameter1,price1)
unitPrice2 = pizzaCalculator(diameter2,price2)

if unitPrice1 > unitPrice2:
    print("The first pizza provides better value for money.")
elif unitPrice1 < unitPrice2:
    print("The second pizza provides better value for money.")
elif unitPrice1 == unitPrice2:
    print("The two pizza provides the same value for money.")