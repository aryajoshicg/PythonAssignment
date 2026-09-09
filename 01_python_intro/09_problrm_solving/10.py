age = int(input("Enter your age:"))

if age > 120 or age < 0:
    print("INvalid age")

elif age < 18:
    print("Cannot vote")

else :
    print("Can vote")        