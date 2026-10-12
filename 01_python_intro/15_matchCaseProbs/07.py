menu2 = int(input("The available options are: 1 Acount Balance, 2 Mini statement, 3 Fund transfer, 4 Bill payment, 5 Customer support: "))
match menu2:
    case 1:
        print("Opening Acount balance")
    case 2:
        print("Opening Mini statement")
    case 3:
        print("Opening Fund transfer")
    case 4:
        print("Opening Bill payment")
    case 5:
        print("Opening customer support")
    case _:
        print("Invalid setting")