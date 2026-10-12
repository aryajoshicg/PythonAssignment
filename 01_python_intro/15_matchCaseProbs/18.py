category = input("Enter a category: ")
match category:
    case "electronics":
        role = int(input("Enter a number: "))
        match role:
            case 1:
                print("Mobile")
            case 2:
                print("laptop")
            case 3:
                print("headphones")
    case "clothing":
        role2 = int(input("Enter a number: "))
        match role2:
            case 1:
                print("shirt")
            case 2:
                print("jeans")
            case 3:
                print("shoes")
    case _:
        print("Invalid input")