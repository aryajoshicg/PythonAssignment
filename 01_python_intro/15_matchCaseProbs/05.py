menu2 = int(input("The available options are: 1 View profile, 2 View courses, 3 View marks, 4 View attendence, 5 Logout: "))
match menu2:
    case 1:
        print("Student details")
    case 2:
        print("Curriculum and Syllabus")
    case 3:
        print("Opening marks")
    case 4:
        print("Attendence percent")
    case 5:
        print("Exit")
    case _:
        print("Invalid setting")