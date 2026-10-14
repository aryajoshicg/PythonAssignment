#problem 1
# while True:
#     marks = int(input("Enter your marks: "))
#     if marks<=100 and marks>=0:
#         print("Valid marks")
#         break
#     else:
#         print("Invalid marks, try again!")

#problem 2
# while True:
#     num = int(input("Enter a number: "))
#     if num>0:
#         print("Accepted number")
#         break
#     else:
#         print("Unaccepted, try again")

#problem 3
# while True:
#     age = int(input("Enter your age: "))
#     if age>0 and age<=120:
#         print("Accepted")
#         break
#     else:
#         print("Not accepted, try again")

#problem 4
# while True:
#     menu = int(input("Enter a numner: "))
#     if menu==1:
#         print("View Profile")
#         break
#     elif menu==2:
#         print("Edit profile")
#         break
#     elif menu==3:
#         print("Settings")
#         break
#     elif menu==4:
#         print("Exit")
#         break
#     else:
#         print("Invalid input, try again")

#problem 5
# while True:
#     password = input("Enter a strong password: ")
#     if len(password.strip())>=8:
#         print("Valid")
#         break
#     else:
#         print("Not valid, try again")

#problem 6
# while True:
#     temp = int(input("Enter the temperature: "))
#     if temp>=-20 and temp<=45:
#         print("Valid temperature")
#         break
#     else:
#         print("Invalid temperature, try again")

#problem 7
# bank_balance = 5000
# while True:
#     withdrawal = int(input("Enter the withdrawal amount: "))
#     if 0<=withdrawal<=bank_balance:
#         print("Valid amount")
#         break
#     else:
#         print("Not valid, try again")

#problem 8
# while True:
#     username = input("Enter a username: ").strip()
#     if len(username)>=5:
#         print("Valid")
#         break
#     else:
#         print("Invalid, try again")

#problem 9
# while True:
#     num = int(input("Enter a number dividible by both 3 and 5: "))
#     if num%3==0 and num%5==0:
#         print("Valid input")
#         break
#     else:
#         print("Invalid input, try again")

#problem 10
# secret_pin = 2468
# for i in range(3):
#     pin = int(input("Enter your pin: "))
#     if pin == secret_pin:
#         print("Valid")
#         break
#     else:
#         print("Invalid pin, try again")

#problem 11
# while True:
#     num = int(input("Enter a number: "))
#     if num>=10 and num<=50:
#         print("Valid value")
#         break
#     else:
#         print("Invalid input, try again!")

#problem 12
balance = 2000
while True:
    deposit = int(input("Enter your deposit amount: "))
    if deposit>0:
        print("Current balance: ",deposit+ balance)
        break
    else:
        print("Invalid input, try again!")








