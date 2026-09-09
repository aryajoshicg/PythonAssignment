day = int(input())
month = int(input())
year = int(input())

# Check if the year is a leap year
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    leap_year = True
else:
    leap_year = False

# Check the number of days based on the month
if month < 1 or month > 12:
    print("Invalid date")

elif month == 2:
    if leap_year:
        if 1 <= day <= 29:
            print("Valid date")
        else:
            print("Invalid date")
    else:
        if 1 <= day <= 28:
            print("Valid date")
        else:
            print("Invalid date")

elif month == 4 or month == 6 or month == 9 or month == 11:
    if 1 <= day <= 30:
        print("Valid date")
    else:
        print("Invalid date")

else:
    if 1 <= day <= 31:
        print("Valid date")
    else:
        print("Invalid date")