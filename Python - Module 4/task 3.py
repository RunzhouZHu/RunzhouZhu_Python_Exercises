max = float()
min = float()
while True:
    i = input("Enter: ")
    if i == '':
        print(f"The program ends, the largest is {max}, the smallest is {min}.")
        break
    else:
        if float(i) > max:
            max = float(i)
        elif float(i) < min:
            min = float(i)        