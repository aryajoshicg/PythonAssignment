dashboard = int(input("Available options: 1 Engine, 2 Lights, 3 Music, 4 Navigation: "))
match dashboard:
    case 1:
        eng = int(input("Available options: 1 Start, 2 Stop: "))
        match eng:
            case 1:
                print("Start")
            case 2:
                print("Stop")
    case 2:
        lig = int(input("Available options: 1 Headlights, 2 Indicators, 3 Hazard Lights: "))
        match lig:
            case 1:
                print("Headlights")
            case 2:
                print("Indicators")
            case 3:
                print("Hazard Lights")
    case 3:
        music = int(input("Available options: 1 Play, 2 Pause, 3 Next, 4 Previous: "))
        match music:
            case 1:
                print("Play")
            case 2:
                print("Pause")
            case 3:
                print("Next")
            case 4:
                print("Previous")
    case 4:
        nav = int(input("Available options: 1 start, 2 stop: "))
        match nav:
            case 1:
                print("Start")
            case 2:
                print("Stop")
    case _:
        print("Invalid Input")