menu = int(input("Available options: 1 Regular, 2 Premium, 3 VIP: "))
match menu:
    case 1:
        age = int(input("Enter your age: "))
        if age<5:
            print("Free entry")
        else:
            print("Regular")
    case 2:
        age = int(input("Enter your age: "))
        if age<5:
            print("Free entry")
        else:
            print("Premium")
    case 3:
        age = int(input("Enter your age: "))
        if age<5:
            print("Free entry")
        else:
            print("VIP")
    case _:
        print("Invalid input")