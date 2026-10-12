system = int(input("Available options: 1 student, 2 teacher, 3 parent: "))
match system:
    case 1:
        menu = int(input("Available options: 1 marks, 2 attendence, 3 homework: "))
        match menu:
            case 1:
                print("Marks selected")
            case 2:
                print("Attendence selected")
            case 3:
                print("Homework selected")
    case 2:
        menu2 = int(input("Available options: 1 enter marks, 2 attendence, 3 assign homework: "))
        match menu2:
            case 1:
                print("Enter marks")
            case 2:
                print("Attendence")
            case 3:
                print("Assign homework")
    case 3:
        menu3 = int(input("Available options: 1 child marks, 2 child attendence, 3 contact teacher: "))
        match menu3:
            case 1:
                print("Child marks")
            case 2:
                print("Child attendence")
            case 3:
                print("Contact teacher")
    case _:
        print("Invalid input")