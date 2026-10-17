#que 01
for i in range(1,4):
    for j in range(1,4):
        print(i,j)

# que 02
N = int(input("Enter a number: "))
for i in range(1,N+1):
    for j in range(1,N+1):
        print(i, "*", j, "=", i*j)

#que 03
word = input("Enter a character: ")
row = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))
for i in range(row):
    for j in range(column):
        print(word, end=" ")
    print()

#que 04
row = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))
for i in range(row):
    for j in range(column):
        print((i,j), end=" ")
    print()

#que 05
N = int(input("Enter number of rows: "))
for i in range(1, N):
    for j in range(1, N):
        print(i, end="")
    print()

#que 06
N = int(input("Enter a number: "))
for i in range(1,N+1):
    for j in range(1,N+1):
        print(j, end="")
    print()

#que 07
N = int(input("Enter a number: "))
for i in range(1,N+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#que 08
N = int(input("Enter a number: "))
for i in range(N, 0, -1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

#que 09
row = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))
for i in range(row):
    for j in range(column):
        print("*", end=" ")
    print()

#que 10
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        if j%2==0:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()
        
        
    

