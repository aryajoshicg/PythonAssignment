system = int(input("Available options: 1 Starters, 2 Main course, 3 Desserts, 4 Drinks: "))
match system:
    case 1:
        menu = int(input("Available starters: 1 Soup, 2 Spring Roll, 3 Garlic Bread: "))
        match menu:
            case 1:
                print("Soup")
            case 2:
                print("Spring Roll")
            case 3:
                print("Garlic Bread")
    case 2:
        menu2 = int(input("Available desserts: 1 Ice cream, 2 Cake, 3 Gulab Jamun: "))
        match menu2:
            case 1:
                print("Ice cream")
            case 2:
                print("Cake")
            case 3:
                print("Gulab Jamun")
    case 3:
        menu3 = int(input("Available drinks: 1 Coffee, 2 Tea, 3 Juice: "))
        match menu3:
            case 1:
                print("Coffee")
            case 2:
                print("Tea")
            case 3:
                print("Juice")