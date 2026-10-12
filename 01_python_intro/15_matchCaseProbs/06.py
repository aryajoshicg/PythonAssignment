menu2 = int(input("The available options are: 1 Electronics, 2 Clothing, 3 Books, 4 Grocery, 5 Exit: "))
match menu2:
    case 1:
        print("Opening Electronics")
    case 2:
        print("Opening Clothing")
    case 3:
        print("Opening Books")
    case 4:
        print("Opening Grocery")
    case 5:
        print("Exit")
    case _:
        print("Invalid setting")