menu = int(input("Available options: 1 Personal banking, 2 Business banking: "))
match menu:
    case 1:
        menu2 = int(input("Available options: 1 Balance, 2 Transfer, 3 Loan: "))
        match menu2:
            case 1:
                print("Personal Balance")
            case 2:
                print("Personal Transfer")
            case 3:
                print("Personal Loan")
    case 2:
        menu3 = int(input("Available options: 1 Balance, 2 Payroll, 3 Loan: "))
        match menu3:
            case 1:
                print("Business Balance")
            case 2:
                print("Business Payroll")
            case 3:
                print("Business Loan")
    case _:
        print("Invalid input")