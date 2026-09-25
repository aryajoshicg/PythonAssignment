#Que 01(doubttt)
# sentence = input("Enter a sentence: ")

# upper = 0
# lower = 0
# digit = 0
# space = 0
# special = 0

# for ch in sentence:
#     if ch >= 'A' and ch <= 'Z':
#         upper = upper + 1
#     aage kya karna hai???

#Que 02
# fail = 0
# passed = 0
# good = 0
# excellent = 0






#Que 03 (doubt)
# sentence = input("Enter a sentence: ")

# words = sentence.split()

# highest_score = 0
# highest_word = ""

# for word in words:
#     score = 0

#     for ch in word:
     #doubt


#que 04 (doubt)
# for i in range(5):
#     password = input("Enter password: ")

#     length = 0
#     uppercase = 0
#     lowercase = 0
#     digit = 0
#     special = 0

#     for ch in password:
#         length = length + 1

#         if ch >= 'A' and ch <= 'Z':
#             uppercase = 1
#         elif ch >= 'a' and ch <= 'z':
#             lowercase = 1
#         elif ch >= '0' and ch <= '9':
#             digit = 1
#         else:
#             special = 1
#doubt

    
# Que 05
# sentence = input("Enter a sentence: ")

# words = sentence.split()

# short = 0
# medium = 0
# long = 0

# for word in words:
#     length = 0

#     for ch in word:
#         length = length + 1

#     print(word, "Length:", length)

#     if length <= 3:
#         print("Short")
#         short = short + 1

#     elif length >= 4 and length <= 6:
#         print("Medium")
#         medium = medium + 1

#     else:
#         print("Long")
#         long = long + 1

# print("Number of Short words:", short)
# print("Number of Medium words:", medium)
# print("Number of Long words:", long)


#que 6 (issue)
# num = input("Enter a number")

# for i in range(5):
#     even = 0
#     odd = 0

#     for digit in num:
#         if digit in "02468":
#             even = even + 1
#         else:
#             odd = odd + 1

#     print("Even digits:". even)
#     print("Odd digits:", odd)


#     if even > odd:
#         print("Even occurs more")
#     elif odd > even:
#         print("Odd occurs more")
#     else:
#         print("Equal")     

#         ISSUE               

#que 7
# word = input("Enter a string: ")

# for ch in word:
#     count = 0

#     for i in word:
#         if ch == i:
#             count = count + 1

#     if count > 1:
#         print(ch, "=", count, end=" ")

#         if count == 2:
#             print("Duplicate")
#         elif count >= 3 and count <= 4:
#             print("Repeated")

#         else:
#             print("Highly repeated")   
# 
# 
# #Que 08
# total = 0
# budget = 0
# regular = 0
# premium = 0
# luxury = 0

# for i in range(8):
#     price = float(input("Enter price of product: "))

#     total = total + price

#     if price < 500:
#         print("Budget")
#         budget = budget + 1

#     elif price >= 500 and price <= 1999:
#         print("Regular")
#         regular = regular + 1

#     elif price >= 2000 and price <= 4999:
#         print("Premium")
#         premium = premium+1

#     else:
#         print("Luxury")   
#         luxury = luxury +1

# average = total / 8

# print("Total amount:", total)
# print("Budget products:", budget)
# print("Regular products:", regular)
# print("Premium products:", premium)
# print("Luxury products:", luxury)
# print("Average product price:", average)


      
#que 09
# word = input("Enter a string: ")

# vowel = 0
# consonant = 0
# digit = 0
# special = 0
# position =0

# for ch in word:
#     if position%2 == 0:
#         pos_type = "Even"

#     else:
#         pos_type = "Odd"

#     if ch in "aeiouAEIOU":
#         category = "Vowel"
#         vowel = vowel + 1

#     elif (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
#         category = "Consonant"
#         consonant = consonant + 1

#     elif ch >= '0' and ch <= '9':
#         category = "Digit"
#         digit = digit + 1

#     else:
#         category = "Special character"
#         special = special + 1

#     print("Character:", ch,
#           "Position:", position,
#           pos_type,
#           category)

#     position = position + 1


# print()
# print("Vowels:", vowel)
# print("Consonants:", consonant)
# print("Digits:", digit)
# print("Special characters:", special)     


#que 10 (DOUBT)
# n = int(input("Enter n: "))

# for i in range(1, n + 1):
   


# que 11 (DOUBT)
# for i in range(5):
#     username = input("Enter username: ")

#     length = 0
#     digits = 0
#     underscores = 0
#     invalid_special = 0

#     for ch in username:
#         length = length + 1

#         if ch >= '0' and ch <= '9':
#             digits = digits + 1

#         elif ch == '_':
#             underscores = underscores + 1

#         elif (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
#             pass

#         else:
#             invalid_special = invalid_special + 1


#     print("Username:", username)
#     print("Length:", length)
#     print("First character:", username[0])
#     print("Digits:", digits)
#     print("Underscores:", underscores)
#     print("Invalid special characters:", invalid_special)


#que 12
# vowels = 0
# consonants = 0

# sent = input("Enter a sentence: ")

# a_count = 0
# e_count = 0
# i_count = 0
# o_count = 0
# u_count = 0

# for ch in sentence:

#     if ch ...


#que 13
# total_revenue = 0

# for i in range(6):
#     units = int(input("Enter electricity units: "))

#     if units <= 100:
#         bill = units * 5

#     elif units <= 200:
#         bill = (100 * 5) + ((units - 100) * 7)

#     elif units <= 400:
#         bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

#     else:
#         bill = (100 * 5) + (100 * 7) + (200 * 10) + ((units - 400) * 15)

#     print("Bill:", bill)

#     if bill < 1000:
#         print("Low")

#     elif bill <= 3000:
#         print("Medium")

#     else:
#         print("High")

#     total_revenue = total_revenue + bill

# print("Total revenue:", total_revenue)


#que 14
# sentence = input("Enter a sentence: ")

# words = sentence.split()

# for word in words:
#     vowels = 0
#     consonants = 0

#     for ch in word:
#         if ch in "aeiouAEIOU":
#             vowels = vowels + 1

#         elif (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
#             consonants = consonants + 1

#     if vowels > consonants:
#         result = "Vowel Heavy"
#     elif consonants > vowels:
#         result = "Consonant Heavy"
#     else:
#         result = "Balanced"

#     print(word, "->", result)


#que 15
# even = 0
# odd = 0
# positive = 0
# negative = 0
# zero = 0

# largest = 0

# for i in range(3):
#     for j in range(3):
#         num = int(input("Enter number: "))

# DOUBT