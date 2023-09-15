'''
#Question 1
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

########################################
#Question 2
def add_name(name,names):
    if name in names:
        print("Existing name")
    else:
        names.add(name)
        print("New name")
    
names = set()
while True:
    i = input("Please enter a name: ")
    if i == '':
        for x in names:
            print(x)
        break
    else:
        add_name(i,names)
'''    
########################################
#Question 3
def new_airport(ICAO,name,airports):
    airports[ICAO] = name
    
def fetch_airport(ICAO,airports):
    name = airports[ICAO]
    return name

airports = {}
while True:
    print("\nOptions:")
    print("Enter 1 to enter a new airport.")
    print("Enter 2 to fetch airport information.")
    print("Enter any other thing to quit.")
    i = input("Please enter your choice: ")
    
    if i == '1':
        print("\nNew airport: ")
        ICAO = input("Please enter the ICAO code: ")
        name = input("Please enter the name: ")
        if ICAO in airports:
            print("ICAO already exists.")
        elif name in airports:
            print("Name already exists.")
        else:
            new_airport(ICAO,name,airports)
            print("Airport added.")
        
    elif i == '2':
        print("\nFetch information: ")
        ICAO = input("Please enter the ICAO code: ")
        if ICAO in airports:
            print(f"The airport is {fetch_airport(ICAO,airports)}.")
        else:
            print("ICAO not exists.")
        
    else:
        print("END")
        break
            
            
        

    



