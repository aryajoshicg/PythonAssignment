cost = int(input("Enter cost price:"))
selling = int(input("Enter selling price:"))

if cost > selling:
    print("Loss")

elif cost < selling:
    print("Profit")

else:
    print("No profit no loss")       