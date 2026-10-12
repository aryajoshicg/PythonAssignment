portal = int(input("Available options: 1 Employee, 2 Manager: "))
match portal:
    case 1:
        emp = int(input("Available options: 1 View Profile, 2 Apply Leave, 3 View Salary: "))
        match emp:
            case 1:
                print("View Profile")
            case 2:
                apply_leave = int(input("Enter number of days: "))
                if apply_leave<=0:
                    print("Invalid Input")
                else:
                    print("Leave Request Submitted")
            case 3:
                print("View Salary")
    case 2:
        man = int(input("Available options: 1 View team, 2 Approve Leave, 3 View reports: "))
        match man:
            case 1:
                print("View Team")
            case 2:
                print("Approve Leave")
            case 3:
                print("View Reports")
    case _:
        print("Invalid Input")