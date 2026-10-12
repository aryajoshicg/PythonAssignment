menu2 = int(input("The available options are: 1 Check balance, 2 Withdraw money, 3 Deposit money, 4 Change PIN, 5 Exit: "))
match menu2:
    case 1:
        print("Check balance")
    case 2:
        print("Withdraw money")
    case 3:
        print("Deposit money")
    case 4:
        print("Change PIN")
    case 5:
        print("Exit")
    case _:
        print("Invalid setting")