age = int(input())
marks = int(input())
income = int(input())
attendance = float(input())

failed = False

if age < 18 or age > 25:
    print("Reason: Age must be between 18 and 25")
    failed = True

if marks < 85:
    print("Reason: Marks below 85")
    failed = True

if attendance < 75:
    print("Reason: Attendance below 75%")
    failed = True

if income > 300000:
    print("Reason: Family income above ₹300000")
    failed = True

if failed:
    print("Scholarship Rejected")
else:
    print("Scholarship Approved")