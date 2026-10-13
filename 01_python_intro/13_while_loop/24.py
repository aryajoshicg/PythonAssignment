string = input("Enter a string: ")
i = 0
count = 0
while i < len(string):
    if string[i] == 'a':
        count += 1
    i += 1
print("The character 'a' appears", count, "times.")