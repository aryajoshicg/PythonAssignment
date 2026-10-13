#que 1
num = int(input("Enter a number: "))
if num%2==0:
    print("Even")
else:
    print("Odd")


#que 2
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print("Invalid input")


#que 3
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
if num1 > num2 and num1 > num3:
    print(num1)
elif num1 < num2 and num3 < num2:
    print(num2)
elif num3 > num1 and num3 > num2:
    print(num3)
else:
    print("Invalid input")


#que 4
num = int(input("Enter a number: "))
if num>0:
    print("Positive")
elif num<0:
    print("Negetive")
else:
    print("Zero")


#que 5
age = int(input("Enter your age: "))
if age>0 and age<=12:
    print("Child")
elif age>12 and age<=19:
    print("Teenager")
else:
    print("Adult")


#que 6
marks = int(input("Enter your marks: "))
if marks>=90 and marks<=100:
    print("A")
elif marks>=80 and marks<=89:
    print("B")
elif marks>=70 and marks<=79:
    print("C")
elif marks>=60 and marks<=69:
    print("D")
else:
    print("F")


#que 7
num = int(input("Enter a number: "))
if num%5==0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")


#que 8
num = int(input("Enter a number: "))
if num%5==0 and num%3==0:
    print("Divisible by 3 and 5")
else:
    print("Not divisible by 3 and 5")


#que 9
year = int(input("Enter a year: "))
if year%4==0:
    print("Leap year")
else:
    print("Not a leap year")


#que 10
num = int(input("Enter a number: "))
if num>=10 and num<=50:
    print("in range")
else:
    print("out of range")