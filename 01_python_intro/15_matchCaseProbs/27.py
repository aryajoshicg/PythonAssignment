menu = int(input("Available menu: 1 General medicine, 2 Cardiology, 3 Orthopedics, 4 Pediatrics, 5 Emergency: "))
match menu:
    case 1:
        print("General medicine selected")
    case 2:
        print("Cardiology selected")
    case 3:
        print("Orthopedics selected")
    case 4:
        print("Pediatrics selected")
    case 5:
        print("Emergency")
    case _:
        print("Invalid input") 