print("Please select operation")
print("Add")
print("Multiply")
print("Divide")

while True:
    choice = input("select operation from 1,2,3,4 : ")
    if choice in ("1","2","3","4"):
        try:
            number1 = float(input("Enter first number : "))
            number2 = float(input("Enter second number : "))
        except ValueError:
            print("Plear enter number only")
            continue
        if choice == "1" :
            print(f'{number1} + {number2} = {number1 + number2}')
        elif choice == "2" :
                    print(f'{number1} - {number2} = {number1 - number2}')
        elif choice == "3" :
                    print(f'{number1} x {number2} = {number1 * number2}')
        elif choice == "4" :
            if number2 == 0:
                print("connot divide by zero")
            else:
                print(f'{number1} - {number2} = {number1 % number2}')
        break
    else:
        print("Please enter a valid operation choice 1-4 only")