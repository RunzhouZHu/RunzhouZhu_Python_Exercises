def removeOddNumbers(lst):
    
    return [num for num in lst if num % 2 == 0]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original list:", lst)
even_lst = removeOddNumbers(lst)
print("List with odd numbers removed:", even_lst)