lst=[]
while True:
    a = input("")
    if a != '':
        lst = lst.append(a)
    else:
        for x in lst:
            print(x)