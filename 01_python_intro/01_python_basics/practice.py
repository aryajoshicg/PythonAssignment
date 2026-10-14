#a="python"
#b=" python "
#print(b.rstrip())
#print("Hello\nworld")
#print("C:Panda\tikes\nleeping")
#a= "apple apple apple"
#b= "mango"


# print(a == b)
# print(a.replace("apple",))
# print("abc"<"ab")
# print(" " and None)
# print(" " or None)
# print("operation \n  Addition \n Subtraction \n Multiplication \n Division")
# print(input("Enter your operation"))
# number1 = int(input("Enter number 1:"))
# number2 = int(input("Enter number 2:"))
# if number == ("")


# a = 232
# x = a // 10
# y = a % 10
# z = x - 18
# print(x)
# print(y)
# print(z)
# print(y + z)


# for i in range(1,23):
#     print(i, end=" ")


# number = int(input("Enter a number:"))
# for i in range(1,number+1):
#     if number %2 ==0:
#         print("number is even")


# num = int(input("Table of:"))
# for i in range(1,11):
#         print(num*i)


# name = input("Enter a string: ").strip().lower()
# length = len(name)
# eman=""
# for n in range(length-1, -1, -1):
#     eman=eman+name[n]
# if name == eman:
#     print("String is a palindrome")
# else :
#     print("Not a palindrome")


# name = "Python"
# for character in name:
#     print(character)
# for i in range(4):
#     for j in range(2):
#         print(i,j)
# for i in range(4):
#     for j in range(4):
#         print("*", end=" ")
#     print("")
# for i in range(8):
#     for j in range(5):
#         print("*", end=" ")
#     print()    
# for i in range(1,6):
#     space = " " * (6 - i)
#     star = "*" * (i)
#     print(space + star)
# for i in range(1,6):
#     star = "*" * (6 - i)
#     space = " " * (i)
#     print(space + star)
# for i in range(5, 0, -1):
#     for j in range(5 - i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()



#ipo, algorithms, flow chart
# total = 0
# Passed= True
# grade = ""
# for i in range(5):
#     marks = int(input("Enter marks:"))
    

# for i in range
# num = int(input("Enter a number: "))
# for i in range(1, num+1):
#     for j in range(1, num+1):
#         if j==1 or j==num or i==num:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()     


# num = int(input("Enter a number: "))
# for i in range(1, num+1):
#     for j in range(1, num+1):
#         if j==1 or j==num or i==num or i%3==0==j%3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()               


#practice - while loop
# i = 2
# while i <=20:
#     print(i)
#     i += 2


# name = input("Enter string: ")
# i = name
# while i > 0:
#     print(i)
#     i -=1


# string = input("Enter a string: ")
# rstr = ""
# i = len(string) - 1
# while i >= 0:
#     rstr += string[i]
#     i -= 1
# if string == rstr:
#     print("String is pelindrome")
# else:
#     print("string is not pelindrome")
#     print("string reversed: ", rstr)


# string = input("Enter a string: ")
# Flag = True
# i = 0
# j = 6
# while i < j:
#     if string[i] == string[j]:
#         i = i +1
#         j = j -1
# if Flag == True:
#     print("string is palindrome")
# else:
#     print("string is not palindrome")


# str5 = input("Enter a string: ")
# Flag = True
# while (i<j)


# number = int(input("Enter a number: "))
# while number > 0:
#     digit = number% 10
#     print(digit)
#     number = number//10

# number = int(input("Enter a number: "))
# reverse = 0
# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     number = number // 10
# print("Reverse:", reverse)

# number = int(input("Enter a number: "))
# reverse = 0
# while number != 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     if number > 0:
#         number = number // 10
#     else:
#         number = number // -10
# print("Reverse:", reverse)

row = 1

# while row <= 3:
#     column = 1

#     while column <= 4:
#         print("*", end="")
#         column = column + 1

#     print()
#     row = row + 1

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# operator = int(input("Menu: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, Now enter a number: "))
# match operator:
#     case 1:
#         print(num1 + num2)
#     case 2:
#         print(num1 - num2)
#     case 3:
#         print(num1 * num2)
#     case 4:
#         print(num1 / num2)
#     case _:
#         print("Invalid")


# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# operator = input("Available options: +, -, *. /: ")
# match operator:
#     case "+":
#         print(num1 + num2)
#     case "-":
#         print(num1 - num2)
#     case "*":
#         print(num1 * num2)
#     case "/":
#         print(num1 / num2)
#     case _:
#         print("Invalid")


# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# menu = int(input("Available options: +, -, *, exit: ")) 

# while num1>0 and num2>0:
#     if menu == "+":
#         print(num1 + num2)
#         menu = int(input("Available options: +, -, *, /: ")) 
#     if menu == "-":
#             print(num1 - num2)
#             menu = int(input("Available options: +, -, *, /: "))
#     if menu == "":
#             print(num1 * num2)
#             menu = int(input("Available options: +, -, *, /: ")) 
#     if menu == "exit":
#             print("Exit")
#             menu = int(input("Available options: +, -, *, /: "))
# print()

# n = int(7.9)   
# # m = int("7")
# print(n,m) 

# message = """Hello
# Welcome to Python
# Learn Strings"""
# print(message)

# w = "python"
# print(w[0: :2])

# a = 18
# "b" = +a
# print(f"b: {a}")

# a = 7
# b = 9
# print(f"the num {a} is not {b}")
# print(f"tot is {a+b}")
# p = "pu ud wj"
# print(p.split())
# n = ["a", "b"]
# print(" ".join(n))

# text = "Hello"

# print(text + " World")
# print(text * 3)

# age = 20
# is_student = True
# has_id = False
# print(age >= 18 and is_student) or has_id

# name = input("Enter your name: ")
# print(name*3)

# age = input("Enter age: ")
# print(type(age))

# name = input("Name: ")
# age = input("Age: ")
# city = input("City: ")
# print(name, age, city)

# price = 99.5678
# print(f"{price:.6f}")

# a = int(input("Enter: "))
# b = int(input("Enter: "))
# result = a + b
# print(result)

# for number in range(1, 6):
#     print("*")

# word = "Aarya"
# for character in word:
#     print(character)

# for row in range(1,5):
#     for column in range(1, row+1):
#         print("*", end=" ")
#     print()    

# total = 0
# for i in range(1,7):
#     total = total + i
#     print(total)

# count = 2
# while count>=-7:
#     print(count)
#     count=count-1

# num = int(input("Enter a num: "))
# while num != 0:
#     print("you entered: ", num)
#     num = int(input("Enter a number: "))

# for i in range(1,71):
#     if i%7==0:
#         print(i)

# sum = 0 
# for i in range (1,101):
#     sum = sum +1
# print(sum)    

# for i in range(1,11):
#     print(7, "*", i, "=", 7*i)

# str1 = "Python"
# for character in "Python":
#     print(character)

# count = 0
# for i in range(1,51):
#     if i%2==0:
#         count += 1
#         print(i)
# print("Count is: " ,count)

# num = int(input("Enter a num: "))
# factorial = 1
# for i in range(1, num+1)
#     factorial = factorial +1
# print("Factorial: ")

# print(12)
# print("12")
# Print(12)
# a = "python"
# a[4] = "b"

# num = int(input("Enter a number: "))
# menu = "Available options: 1 Even, 2 Odd, 3 Prime"
# match num:
#     case 1:
#         if num%2==0:
#             print("Even")
#     case 2:
#         if num%2==1:
#             print("Odd")
#     case 3:
#         if num%num==0:
#             print("Prime")
#     case _:
#         print()

# day = 7
# match day:
#     case 1 | 2 | 3 | 4:
#         print("Weekday")
#     case 6 | 7:
#         print("Weekend")
#     case _:
#         print("Leave")

# menu = 2
# match menu:
#     case x if x==1:
#         print("Continue in Hindi")
#     case x if x==2:
#         print("Continue in English")
#     case x if x==3:
#         print("Continue in Marathi")
#     case x if x==4:
#         print("Continue in Gujarati")

# menu = 4
# match menu:
#     case x if x==1:
#         print("To slap someone")
#     case x if x==2:
#         print("To kick someone")
#     case x if x==3:
#         print("To punch someone")
#     case x if x==4:
#         print("To kill someone")

# str2 = input("Enter a string: ")
# l = len(str2)
# for i in str2:
#     n = str2.find("o")
#     print("found o") WRONG

# str = input("Enter a string: ").strip().lower()
# flag=True
# count=0
# for ch in str:





# for i in range(1,11):
#     if i == 6:
#         break
#     print(i)

# number = [10, 20, 30, 40, 50]
# for i in number:
#     if number!=30:
#         break
#     print("found", i)

# num = input("Enter a number: ")
# for i in num:
#     if i != 0:
#         print("Enter a num: ")
#     if i == 0:
#         break
# print(i)

# for i in range(1,101):
#     if i%17==0:
#         break
#     print(i)

# for i in range(1,21):
#     if i%2==0:
#         continue
#     print(i)

# numbers = [10, -2, 30, -5, 40, -8]
# for n in numbers:
#     if n<0:
#         continue
#     print(n)

# for k in range(1,21):
#     if k%3==0:
#         continue
#     print(k)

# numbers = [5, 12, 8, 21, 30, 7]
# for z in numbers:
#     if z <= 10:
#         continue
#     print(z)

# x = 10
# if x > 5:
#     pass
# print("Program finished")

# for i in range(1,6):
#     if i==3:
#         break
#     print(i)

# for k in range(1,6):
#     if k==3:
#         continue
#     print(k)

# for j in range(1,6):
#     if j==3:
#         pass
#     print(j)

# i = 1
# while i<=5:
#     if i==3:
#         continue
#     print(i)
#     i+=1

# for i in range(1, 5):
#     if i == 2:
#         pass
#     elif i == 3:
#         continue
#     elif i == 4:
#         break
#     print(i)

# for i in range(1, 6):
#     if i == 3:
#         break
# else:
#     print("Done")

# for i in range(1,6):
#     if i ==3:
#         continue
#     else:
#         print("Done")











# def addition():
#     num = int(input("Enter a number: "))
#     num2 = int(input("Enter a number: "))
#     print(num + num2)

# def subtraction():
#     num3 = int(input("Enter a number: "))
#     num4 = int(input("Enter a number: "))
#     print(num3 - num4)

# def multiplication():
#     num5 = int(input("Enter a number: "))
#     num6 = int(input("Enter a number: "))
#     print(num5 * num6)

# def floor_division():
#     num7 = int(input("Enter a number: "))
#     num8 = int(input("Enter a number: "))
#     print(num7 // num8)

# addition()
# subtraction()
# multiplication()
# floor_division()

# def even_odd():
#     num9 = int(input("Enter a num: "))
#     if num9%2==0:
#         print("Even")
#     else:
#         print("Odd")

# even_odd()

# def prime_composite():
#     num = int(input("Enter a number: "))
#     if num%

# for i in range(1, 5):
#     print("X", end="")
#     if i == 2:
#         continue
#     print("Y", end="")
# print("Z")

# acc_balance = 30000
# def check_balance():
#     print("Current balance:",acc_balance)

# def credit_balance():
#     num = int(input("Enter the amount: "))
#     print("Amount credited successfully! Current balance: ", acc_balance+num)

# def withdrawal_balance():
#     num = int(input("Enter the amount: "))
#     if num>30000:
#         print("Insufficient balance, try again!")
#     else:
#         print("Amount withdrawal successful! Current balance: ", acc_balance-num)

# menu = int(input("Available options: 1 check balance, 2 credit balance, 3 withdrawal: "))
# match menu:
#     case 1:
#         check_balance()
#     case 2:
#         credit_balance()
#     case 3:
#         withdrawal_balance()
#     case _:
#         print("Invalid input")


# a = 8
# b = 65
# def multiply(a,b):
#     b = "Python is an interpreted language"
#     return a*b

# print(multiply(a,b))

a = 10
b = 20
c = 40
d = 3
def add(a,b):
    c = a + b
    return c
def sub(a, b):
    return a-b
def multi(a,b):
    return abs(a*b)

print(multi(sub(add(a,b),c),d))