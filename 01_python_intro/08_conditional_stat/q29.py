is_student = bool(input("are you a student:"))
has_id = bool(input("do you have your id:"))
has_ticket = bool(input("do you have your ticket:"))

if is_student == True and has_id == True and has_ticket == True:
    print("Allowed")