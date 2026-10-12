menu = int(input("Available options: 1 Student, 2 Teacher, 3 Administration: "))
match menu:
    case 1:
        menu2 = int(input("Available options: 1 Profile, 2 Marks, 3 Attendence, 4 Courses: "))
        match menu2:
            case 1:
                print("Profile")
            case 2:
                print("Marks")
            case 3:
                print("Attendence")
            case 4:
                print("Courses")
    case 2:
        menu3 = int(input("Available options: 1 Students, 2 Enter Marks, 3 Attendence, 4 Courses: "))
        match menu3:
            case 1:
                print("Students")
            case 2:
                print("Enter Marks")
            case 3:
                print("Attendence")
            case 4:
                print("Courses")
    case 3:
        menu4 = int(input("Available options: 1 Fees, 2 Admissions, 3 Notices, 4 Departments: "))
        match menu4:
            case 1:
                print("Fees")
            case 2:
                print("Admissions")
            case 3:
                print("Notices")
            case 4:
                print("Departments")
    case _:
        print("Invalid Input")