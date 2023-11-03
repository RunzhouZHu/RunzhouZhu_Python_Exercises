talents = float(input("Enter talents: \n\n"))
pounds = float(input("Enter pounds: \n\n"))
lots = float(input("Enter lots: \n\n"))

g = 13.3 * (32 * (20 * talents + pounds) + lots)
kilograms = int(g / 1000)
grams = round(g - 1000 * kilograms, 2)

print(f"The weight in modern units:\n{kilograms} kilograms and {grams} grams.")