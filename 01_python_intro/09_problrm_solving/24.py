purchase = float(input())

if purchase < 500:
    discount_percent = 0
elif purchase < 1000:
    discount_percent = 5
elif purchase < 2000:
    discount_percent = 10
elif purchase < 5000:
    discount_percent = 15
else:
    discount_percent = 20

discount_amount = purchase * discount_percent / 100
final_amount = purchase - discount_amount

print("Original amount:", purchase)
print("Discount percentage:", discount_percent, "%")
print("Discount amount:", discount_amount)
print("Final amount:", final_amount)