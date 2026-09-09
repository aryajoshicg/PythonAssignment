marks1 = int(input())
marks2 = int(input())
marks3 = int(input())

# Check whether marks are between 0 and 100
if (marks1 < 0 or marks1 > 100 or
    marks2 < 0 or marks2 > 100 or
    marks3 < 0 or marks3 > 100):
    print("Invalid marks")

# Check whether every subject is passed
elif marks1 < 35 or marks2 < 35 or marks3 < 35:
    print("Fail")

else:
    average = (marks1 + marks2 + marks3) / 3

    print("Average:", average)

    if average >= 75:
        print("Distinction")
    elif average >= 60:
        print("First Class")
    elif average >= 50:
        print("Second Class")
    else:
        print("Pass")