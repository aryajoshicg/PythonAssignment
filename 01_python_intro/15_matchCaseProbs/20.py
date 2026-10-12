num = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
operator = input("Available operators are +, -, *, /: ")
match operator:
    case "+":
        print(num + num2)
    case "-":
        print(num - num2)
    case "*":
        print(num * num2)
    case "/":
        print(num / num2)
    case _:
        print("Invalid input")