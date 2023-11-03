n = int(input("Please enter a interger: "))
for x in range(2,n-1):
    if n % x == 0:
        print("This is not a prime number.")
        break
    else:
        print("This is a prime number.")
        break