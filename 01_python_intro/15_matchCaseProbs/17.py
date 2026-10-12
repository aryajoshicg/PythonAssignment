user = int(input("Enter account type: "))
match user:
    case 1:
        operations= int(input("Enter operations: "))
        match operations:
            case 1:
                print("check deposit")
            case 2:
                print("deposit")
            case 3:
                print("withdraw")
    case 2:
        operations2= int(input("Enter operations: "))
        match operations2:
                    case 1:
                        print("check deposit")
                    case 2:
                        print("deposit")
                    case 3:
                        print("withdraw")
    case _:
          print("invalid input")
