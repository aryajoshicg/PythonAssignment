pay_app = int(input("Available options: 1 UPI, 2 Card, 3 Wallet: "))
match pay_app:
    case 1:
        menu = int(input("Available options: 1 Scan QR, 2 Enter UPI ID: "))
        match menu:
            case 1:
                print("Scan QR")
            case 2:
                print("Enter UPI ID")
    case 2:
        menu2 = int(input("Available options: 1 Credit card, 2 Debit card: "))
        match menu2:
            case 1:
                print("Credit Card")
            case 2:
                print("Debit Card")
    case 3:
        menu3 = int(input("Available options: 1 Add money, 2 Pay using wallet"))
        match menu3:
            case 1:
                print("Add Money")
            case 2:
                print("Pay Using Wallet")
    case _:
        print("Invalid Input")