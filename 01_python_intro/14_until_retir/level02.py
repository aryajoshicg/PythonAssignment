#que 11
for i in range(1,11):
    print(i, end=" ")

#que 12
n = int(input("Enter a number: "))
for j in range(1,n+1):
    print(j, end=" ")

#que 13
n = int(input("Enter a number: "))
for x in range(1,n+1):
    if x%2==0:
        print(x, end=" ")

#que 14
n = int(input("Enter a number: "))
for x in range(1,n+1):
    if x%2==1:
        print(x, end=" ")

#que 15
n = int(input("Enter a number: "))
sum=0
for x in range(1,n+1):
    sum += x
print(sum)

#que 16
n = int(input("Enter a number: "))
prod = 1
for x in range(1,n+1):
    prod *=x
print(prod)

#que 17
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n * i, end=" ")

#que 18
n = int(input("Enter a number: "))
for i in range(1, n+1):
    if i%3==0:
        print(i, end=" ")

#que 19
n = int(input("Enter a number: "))
factorial = 1
for i in range(1,n+1):
    factorial *= i
    print(factorial)

#que 20
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(i*7, end=" ")