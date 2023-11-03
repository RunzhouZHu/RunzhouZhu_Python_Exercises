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