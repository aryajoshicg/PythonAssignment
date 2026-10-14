#que 13
# while True:
#     num = int(input("Enter a number between 1 and 100: "))
#     if num>=1 and num<=100:
#         print("Valid value")
#         break
#     else:
#         print("Invalid value, try again!")



#que 14
# while True:
#     marks = int(input("Enter your marks: "))
#     if marks>=75 and marks<=100:
#         print("Distinction!")
#         break
#     elif marks>=60 and marks<=74:
#         print("First Class!")
#         break
#     elif marks>=35 and marks<=59:
#         print("Pass!")
#         break
#     elif marks>=0 and marks<=34:
#         print("Fail!")
#         break
#     else:
#         print("Invalid input, try again!")



#que 15
# while True:
#     username=input("Enter your username: ").strip()
#     password = input("Enter your password: ").strip()
#     if len(username)>=5 and len(password)>=8:
#         print("Welcome to the website!")
#         break
#     else:
#         print("Invalid input, try again!")



#que 16
# while True:
#     num = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     oper = input("Available options: +, -, *, /. Enter the operator: ")
#     if oper == "+":
#         print(num + num2)
#         break
#     elif oper == "-":
#         print(abs(num - num2))
#         break
#     elif oper == "*":
#         print(num * num2)
#         break
#     elif oper == "/" and num2 !=0:
#         print(num / num2)
#         break
#     else:
#         print("Invalid input, try again!")



#que 17
# balance = 10000
# while True:
#     menu = int(input("Available options: 1 Check balance, 2 Deposit money, 3 Withdraw money, 4 Exit: "))
#     match menu:
#         case 1:
#             print(balance)
#         case 2:
#             num = int(input("Enter the deposit amount: "))
#             if num>0:
#                 print("Deposit successful, current balance: ", balance+num)
#             else:
#                 print("Invalid amount, try again!")
#         case 3:
#             num2 = int(input("Enter the withdrawal money: "))
#             if num2>0 and num2<balance:
#                 print("Withdrawal successful! Current balance: ", balance-num2)
#             else:
#                 print("Invalid amount, try again!")
#         case 4:
#             print("Exit!")
#             break
#         case _:
#             print("Invalid input, try again!")


#que 18
# while True:
#     month = int(input("Enter month: "))
#     date = int(input("Enter date: "))
#     if 1<=month<=12 and 1<=date<=31:
#         print("Month number is ", month, "and date number is ", date)
#         break
#     else:
#         print("Invalid input, try again!")


#que 19
# while True:
#     quantity = int(input("Enter the product quantity: "))
#     price = int(input("Enter the product price: "))
#     if quantity>0 and price>0:
#         print("The total would be: ", quantity*price)
#         break
#     else:
#         print("Invalid input, try again!")


#que 20
# while True:
#     n = int(input("Enter a number between 1 and 20: "))
#     if 1<=n<=20:
#         break
#     else:
#         print("Invalid input, try again: ")
# total=0
# for i in range(1,n+1):
#     while True:
#         number=float(input(f"Enter number {i}: "))
#         total += number
#         break
# average=total/n
# print("Average: ", average)


#que 21
# while True:
#     password = input("Enter a strong password: ").strip()
#     if len(password)>=8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
#         print("Valid password")
#         break
#     else:
#         print("Invalid password, try again!")


#que 22
# num = int(input("Enter an integer between 1 and 10: "))
# while num<1 or num>10:
#     num = int(input("Invalid! Enter an integer between 1 and 10: "))

# print("Valid number: ", num)


#que 23
# while True:
#     num = int(input("Enter first score: "))
#     num2 = int(input("Enter second score: "))
#     num3 = int(input("Enter third score: "))
#     if 0<=num<=100 and 0<=num2<=100 and 0<=num3<=100:
#         avg = num + num2 + num3
#         print("The total is: ", avg)
#         print("The average is: ", avg/3)
#         break
#     else:
#         print("Invalid input, try again!")


#que 24
balance = 10000
while True:
    num = int(input("Enter the withdrawal amount: "))
    if num>0 and num<balance and num%100==0:
        print("The amount withdrew is: ", num)
        print("Current balance: ", balance-num)
        break
    else:
        print("Invalid amount, try again!")
