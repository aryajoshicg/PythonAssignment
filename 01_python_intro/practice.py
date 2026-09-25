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

num = int(input("Enter a number: "))
for i in range(1, num+1):
    for j in range(1, num+1):
        if j==1 or j==num or i==num or i%3==0==j%3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()               
