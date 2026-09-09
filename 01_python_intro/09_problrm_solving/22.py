balance = int(input())
withdrawal = int(input())

if withdrawal <= 0:
    print("Invalid withdrawal amount")
elif withdrawal % 100 != 0:
    print("Withdrawal amount must be divisible by 100")
elif withdrawal > balance:
    print("Insufficient balance")
elif balance - withdrawal < 500:
    print("Minimum balance of ₹500 must remain")
else:
    balance = balance - withdrawal
    print("Withdrawal successful")
    print("Remaining balance:", balance)