inche = 0
while True:
    inche = float(input("Please enter the value of inches: "))
    if inche < 0:
        break
    print(f"{inche} inche equals to {inche * 2.54} centimeter."