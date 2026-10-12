menu = int(input("The available options are: 1 Morning show, 2 Afternoon show, 3 Evening show, 4 Night show: "))
match menu:
    case 1:
        print("Morning show selected ")
    case 2:
        print("Afternoon show selected")
    case 3:
        print("Evening show selected")
    case 4:
        print("Night show selected")
    case _:
        print("Invalid setting")