
system = input("Enter role: ").lower()

match system:
    case "admin":
        print("Full access")
    case "teacher":
        print("teacher dashboard")
    case "student":
        print("Student dashboard")
    case "guest":
        print("Limited access")
    case _:
        print("Invalid role")