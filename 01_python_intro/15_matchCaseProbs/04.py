menu2 = int(input("The available options are: 1 red, 2 yellow, 3 green: "))
match menu2:
    case 1:
        print("Stop")
    case 2:
        print("Wait")
    case 3:
        print("Go")
    case _:
        print("Invalid setting")