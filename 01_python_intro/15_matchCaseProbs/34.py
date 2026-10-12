menu =  int(input("Available options: 1 start game, 2 load game, 3 settings, 4 exit: "))
match menu:
    case 1:
        print("Start Game")
    case 2:
        print("Load Game")
    case 3:
        settings = int(input("Settings: 1 Sound, 2 Graphics, 3 Controls: "))
        match settings:
            case 1:
                print("Sound Setting Selected")
            case 2:
                print("Graphics Setting Selected")
            case 3:
                print("Controls Setting Selected")
    case 4:
        print("Exit")
    case _:
        print("Invalid input")