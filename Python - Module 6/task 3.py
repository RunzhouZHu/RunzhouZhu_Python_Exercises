def unitConvert(x):
    y = 3.785 * x
    return y

while True:
    x = float(input("Please enter the volume in gallons: "))
    if x < 0:
        break
    y = unitConvert(x)
    print(y)