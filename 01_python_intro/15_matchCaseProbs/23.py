account = int(input("Available options: 1 Savings, 2 Current: "))
match account:
    case 1:
        amount = int(input("Enter an amount: "))
        if amount>0:
            print("Withdrawal request accepted")
        else:
            print("Invalid input")
    case 2:
        amount = int(input("Enter an amount: "))
        if amount>0:
            print("Withdrawal request accepted")
        else:
            print("Invalid input")
    case _:
        print("Invalid input")