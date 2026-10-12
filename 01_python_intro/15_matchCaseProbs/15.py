membership = int(input("Enter your number: "))
match membership:
    case 1 | 2:
        print("Basic membership")
    case 3 | 4:
        print("Premium membership")
    case _:
        print("Invalid input")