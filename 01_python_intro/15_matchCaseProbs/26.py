controller = int(input("Available options: 1 Light, 2 Fan, 3 AC, 4 TV:  "))
match controller:
    case 1:
        print("Light controller opened")
    case 2:
        print("Fan controller opened")
    case 3:
        print("AC controller opened")
    case 4:
        print("TV controller opened")
    case _:
        print("Invalid input")
