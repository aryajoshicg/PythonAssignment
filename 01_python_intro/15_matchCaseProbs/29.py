menu = int(input("Available options: 1 Search Book, 2 Issue book, 3 Return book, 4 View issued books, 5 Exit: "))
match menu:
    case 1:
        print("Search book")
    case 2:
        print("Issue book")
    case 3:
        print("Return book")
    case 4:
        print("View issued books")
    case 5:
        print("exit")
    case _:
        print("Invalid Input")