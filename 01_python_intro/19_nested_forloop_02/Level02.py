#que 11
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
for i in range(1, rows+1):
    for j in range(1, columns+1):
        if j%2==0:
            print(j, end=" ")
    print()

#que 12
n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if j%2==1:
            print(j,end=" ")
    print()

#que 13
for i in range(1,5):
    for j in range(1,5):
        if (i+j)%2==0:
            print("E", end=" ")
        else:
            print("O", end=" ")
    print()

#que 14
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==j):
            print("Same", end=" ")
        else:
            print("Different", end=" ")
    print()

#que 15
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

#que 16
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%j==0:
            print("X", end=" ")
        else:
            print("-", end=" ")
    print()

#que 17
n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1,n+1):
        if j%i==0:
            print(j, end=" ")
        else:
            pass
    print()


#que 18
n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if (i+j)>n:
            print(i,j)
    print()

#que 19
n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1,n+1):
        if (i*j)%2==0:
            print(i, j, i*j)
    print()

#que 20
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1, n+1):
        if (i==j):
            print("SPECIAL", end=" ")
        elif (i+j)==n:
            print("PAIR", end=" ")
        else:
            print("NORMAL", end=" ")
    print()