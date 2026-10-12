
choice = int(input("Enter choice: "))

match choice:
    case 1:
        temperature = float(input("Enter temperature: "))
        fahrenheit = (temperature * 9 / 5) + 32
        print("Temperature =", fahrenheit, "F")

    case 2:
        temperature = float(input("Enter temperature: "))
        celsius = (temperature - 32) * 5 / 9
        print("Temperature =", celsius, "C")

    case _:
        print("Invalid Choice")