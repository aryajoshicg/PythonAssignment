num = int(input("Enter a number:"))

if num > 0 and num % 2 == 0:
    print("Positive Even")

elif num > 0 and num % 2 == 1:
    print("Postive Odd")

elif num < 0 and num % 2 == 0:
    print("Negetive Even")

elif num < 0 and num % 2 == 1:
    print("Negetive Odd")

else:
    print("ZEro")                