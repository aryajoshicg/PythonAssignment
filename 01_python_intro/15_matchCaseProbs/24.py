menu = int(input("Available options: 1 Start Exam, 2 View Results, 3 Exit: "))
match menu:
    case 1:
        age = int(input("Enter your age: "))
        if age >=18:
            print("You can start the exam")
        else:
            print("Not eligible for exam")
    case 2:
        print("Showing results")
    case 3:
        print("Exit")
    case _:
        print("Invalid input")