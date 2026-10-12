platform = int(input("Available options: 1 Programming, 2 Mathematics, 3 Communication: "))
match platform:
    case 1:
        prog = int(input("Available options: 1 Python, 2 Java, 3 C++: "))
        match prog:
            case 1:
                print("Python")
            case 2:
                print("Java")
            case 3:
                print("C++")
    case 2:
        math = int(input("Available options: 1 Algebra, 2 Calculus, 3 Statistics: "))
        match math:
            case 1:
                print("Algebra")
            case 2:
                print("Calculus")
            case 3:
                print("Statistics")
    case 3:
        comm = int(input("Available options: 1 English, 2 Presentation, 3 Interview Skills: "))
        match comm:
            case 1:
                print("English")
            case 2:
                print("Presentation")
            case 3:
                print("Interview Skills")
    case _:
        print("Invalid Input")