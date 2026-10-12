transport = int(input("Available options: 1 Flight, 2 Train, 3 Bus: "))
match transport:
    case 1:
        class_ = int(input("Available options: 1 Economy, 2 Business: "))
        match class_:
            case 1:
                print("Economy class selected")
            case 2:
                print("Business class selected")
    case 2:
        class_2 = int(input("Available options: 1 Sleeper, 2 AC: "))
        match class_2:
            case 1:
                print("Sleeper class selected")
            case 2:
                print("AC class selected")
    case 3:
        class_3 = int(input("Available options: 1 Ordinary, 2 Volvo: "))
        match class_3:
            case 1:
                print("Ordinary class selected")
            case 2:
                print("Volvo class selected")
    case _:
        print("Invalid input")