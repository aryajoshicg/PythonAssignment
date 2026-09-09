username = input()
password = input()

if username != "admin":
    print("User not found")
elif password != "python123":
    print("Wrong password")
else:
    print("Login successful")