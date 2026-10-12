menu = int(input("Available options: 1 placed, 2 confirmed, 3 preparing, 4 out_for_delivery, 5 delivered, 6 cancelled: "))
match menu:
    case 1:
        print("Book Ticket")
    case 2:
        print("Cancel Ticket")
    case 3:
        print("Check PNR")
    case 4:
        print("Train Schedule")
    case 5:
        print("exit")
    case _:
        print("Invalid Input")