number = int(input())

if number < 0:
    print("Number is Negative")
elif number <= 10:
    print("Number is between 0 and 10")
elif number <= 50:
    print("Number is between 11 and 50")
elif number <= 100:
    print("Number is between 51 and 100")
else:
    print("Number is Above 100")