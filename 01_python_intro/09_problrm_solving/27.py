hours = int(input())
minutes = int(input())
seconds = int(input())

if (0 <= hours <= 23 and
    0 <= minutes <= 59 and
    0 <= seconds <= 59):
    print("Valid time")
else:
    print("Invalid time")