menu = int(input("Available options: 1 Book ticket, 2 Cancel ticket, 3 Check PNR, 4 Train schedule, 5 Exit: "))
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