times = 0
while True:
    username = input("Please enter the username: ")
    password = input("Please enter the password: ")
    if username == "python" and password == "rules":
        print("Welcome")
    else:
        print("Please try again.")
        times = times + 1
    if times == 5:
        print("Access denied")
        break