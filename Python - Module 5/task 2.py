numbers = []
while True:
    n = input("Please enter a number: ")
    if n == '':
        break
    numbers.append(n)
    
i = 0
numbers.sort(reverse=True)
while i < 5:
    print(numbers[i])
    i = i + 1