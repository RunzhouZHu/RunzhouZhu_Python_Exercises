seasons = ("spring", "summer", "autumn", "winter")
def find_season(month):
    if month>=3 and month<=5:
        i = 0
    elif month>=6 and month<=8:
        i = 1
    elif month>=9 and month<=11:
        i = 2
    elif month==12 or 0<=month<=2:
        i = 3
    return seasons[i]

season = int(input("Please enter the number of month: "))
print(f"The season is {find_season(season)}")