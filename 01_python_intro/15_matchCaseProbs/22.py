
choice = int(input("Enter choice: "))

match choice:
    case 1:
        value = float(input("Enter a value: "))
        print(value*1000,"meters")

    case 2:
        value = float(input("Enter a value: "))
        print(value/1000,"kilometers")

    case 3:
        value = float(input("Enter a value: "))
        print(value *1000,"grams")

    case 4:
        value = float(input("Enter a value: "))
        print(value/1000,"kilograms")

    case _:
        print("Invalid Choice")