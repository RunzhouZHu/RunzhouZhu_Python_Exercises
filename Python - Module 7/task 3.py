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
            
            
        

    



