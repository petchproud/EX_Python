rows = int(input("How many rows: "))
colums = int(input("How many colums: "))
row = 0
while row < rows:
    print()
    colum = 0
    while colum < colums:
        colum += 1
        print("*",end="")
    print()
    row += 1