menu2 = int(input("The available options are: 1 Pizza, 2 Burger, 3 Pasta, 4 Sandwich: "))
match menu2:
    case 1:
        print("You selected pizza")
    case 2:
        print("You selected Burger")
    case 3:
        print("You selected Pasta")
    case 4:
        print("You selected Sandwich")
    case _:
        print("Invalid menu choice")