
payment_method = input("Enter Payment method: ").lower()

match payment_method:
    case "upi":
        print("UPI payment selected")
    case "card":
        print("Card payment selected")
    case "cash":
        print("Cash payment selected")
    case "wallet":
        print("Wallet payment selected")
    case _:
        print("Invalid input")