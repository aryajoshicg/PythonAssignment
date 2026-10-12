menu2 = int(input("The available options are: 1 Wi-fi, 2 Bluetooth, 3 Mobile data, 4 Airoplane mode, 5 Exit: "))
match menu2:
    case 1:
        print("You selected Wi-fi")
    case 2:
        print("You selected Bluetooth")
    case 3:
        print("You selected Mobile data")
    case 4:
        print("You selected Airoplane mode")
    case 5:
        print("You selected Exit")
    case _:
        print("Invalid setting")