a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")
    