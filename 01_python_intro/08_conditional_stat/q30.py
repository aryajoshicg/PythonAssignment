age = int(input("Enter your age:"))
marks = int(input("Enter your marks:"))
has_id = bool(input("do you have your id:"))

if age >= 18 and marks >= 40 and has_id == True:
    print("Eligible")

else :
    print("Not Eligible")    