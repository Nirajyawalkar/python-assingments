# <<<<<<< lab assignments 1>>>>>>>>>>
# balance = 0
#
# def deposit(amount):
#     global balance
#     balance += amount
#
# def withdraw(amount):
#     global balance
#     if amount <= balance:
#         balance -= amount
#     else:
#         print("Insufficient balance")
#
# while True:
#     print("\n1.Check Balance 2.Deposit 3.Withdraw 4.Exit")
#     ch = int(input("Enter choice: "))
#
#     if ch == 1:
#         print("Balance:", balance)
#     elif ch == 2:
#         amt = float(input("Enter amount: "))
#         deposit(amt)
#     elif ch == 3:
#         amt = float(input("Enter amount: "))
#         withdraw(amt)
#     else:
#         break

# <<<<<  lab assignments2 >>>>>>>>>..
# def add(a, b): return a + b
# def sub(a, b): return a - b
# def mul(a, b): return a * b
# def div(a, b): return a / b
# def mod(a, b): return a % b
# while True:
#     print("\n1.Add 2.Sub 3.Mul 4.Div 5.Mod 6.Exit")
#     ch = int(input("Enter choice: "))
#
#     if ch == 6:
#         break
#
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#
#     if ch == 1:
#         print(add(a, b))
#     elif ch == 2:
#         print(sub(a, b))
#     elif ch == 3:
#         print(mul(a, b))
#     elif ch == 4:
#         print(div(a, b))
#     elif ch == 5:
#         print(mod(a, b))