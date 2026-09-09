a = int(input())
b = int(input())
c = int(input())

# First check triangle validity
if a + b > c and a + c > b and b + c > a:

    # Check triangle type
    if a == b and b == c:
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Scalene")

else:
    print("Invalid triangle")