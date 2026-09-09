first = int(input())
second = int(input())
operator = input()

if operator == "+":
    print(first + second)

elif operator == "-":
    print(first - second)

elif operator == "*":
    print(first * second)

elif operator == "/":
    if second == 0:
        print("Cannot divide by zero")
    else:
        print(first / second)

else:
    print("Invalid operator")