category = input("Enter a category: ")
match category:
    case "vegetarian":
        role = int(input("Enter a number: "))
        match role:
            case 1:
                print("Paneer")
            case 2:
                print("Dal")
            case 3:
                print("Pulao")
    case "non-vegetarian":
        role2 = int(input("Enter a number: "))
        match role2:
            case 1:
                print("Biryani")
            case 2:
                print("Chicken curry")
            case 3:
                print("Fish curry")
    case _:
        print("Invalid input")