system = int(input("Enter priority number: "))
match system:
    case 1 | 2:
        print("Normal priority")
    case 3 | 4:
        print("Urgent priority")
    case _:
        print("Invalid input")