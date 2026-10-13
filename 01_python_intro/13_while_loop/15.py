n = int(input("Enter a number: "))
i = 1
count = 0
while i <= n:
    if i % 2 ==0:
        count += 1
    i += 1
print("Count of even numbers is: ",count) 