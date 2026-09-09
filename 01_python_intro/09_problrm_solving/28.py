name1 = input()
age1 = int(input())

name2 = input()
age2 = int(input())

name3 = input()
age3 = int(input())

if age1 < age2 and age1 < age3:
    print(name1, "is the youngest")

elif age2 < age1 and age2 < age3:
    print(name2, "is the youngest")

elif age3 < age1 and age3 < age2:
    print(name3, "is the youngest")

elif age1 == age2 and age1 < age3:
    print(name1, "and", name2, "are the youngest")

elif age1 == age3 and age1 < age2:
    print(name1, "and", name3, "are the youngest")

elif age2 == age3 and age2 < age1:
    print(name2, "and", name3, "are the youngest")

else:
    print("All three are the youngest")