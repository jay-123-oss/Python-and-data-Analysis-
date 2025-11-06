print("__________Welcome to the Bank__________")

user = {"jaydeep": 1, "raja": 2, "mohan": 3}
amount = {"jaydeep": 1000, "raja": 1540, "mohan": 1200}

check_login = input("Are you registered (yes/no): ").lower()

if check_login == "yes":
    name = input("Enter your name: ")
    password = int(input("Enter your password: "))

    if name in user:
        if user[name] == password:
            print(f"✅ Welcome {name}, your bank balance is {amount[name]} $")

            while True:
                print("\n1 - Deposit\n2 - Withdraw\n3 - Check Balance\n4 - Exit")
                input1 = int(input("Enter operation: "))

                if input1 == 1:
                    dep = int(input("Enter deposit amount: "))
                    amount[name] += dep
                    print(f"💰 Deposit successful! New Balance = {amount[name]} $")

                elif input1 == 2:
                    withdraw = int(input("Enter withdraw amount: "))
                    if withdraw <= amount[name]:
                        amount[name] -= withdraw
                        print(f"💸 Withdraw successful! New Balance = {amount[name]} $")
                    else:
                        print("❌ Insufficient balance!")

                elif input1 == 3:
                    print(f"📊 Current Balance = {amount[name]} $")

                elif input1 == 4:
                    print("👋 Thank you for using our Bank!")
                    break
                else:
                    print("❌ Invalid option, try again.")
        else:
            print("❌ Wrong password!")
    else:
        print("❌ User not found!")

elif check_login == "no":
    user_name = input("Enter new name: ")
    user_pass = int(input("Enter new password: "))

    user.update({user_name: user_pass})
    amount[user_name] = 0   # new user ko balance bhi dena hai

    print("✅ Registration successful! Please login again.")
    name = input("Enter your name: ")
    password = int(input("Enter your password: "))

    if name in user:
        if user[name] == password:
            print(f"✅ Welcome {name}, your bank balance is {amount[name]} $")

            while True:
                print("\n1 - Deposit\n2 - Withdraw\n3 - Check Balance\n4 - Exit")
                input1 = int(input("Enter operation: "))

                if input1 == 1:
                    dep = int(input("Enter deposit amount: "))
                    amount[name] += dep
                    print(f"💰 Deposit successful! New Balance = {amount[name]} $")

                elif input1 == 2:
                    withdraw = int(input("Enter withdraw amount: "))
                    if withdraw <= amount[name]:
                        amount[name] -= withdraw
                        print(f"💸 Withdraw successful! New Balance = {amount[name]} $")
                    else:
                        print("❌ Insufficient balance!")

                elif input1 == 3:
                    print(f"📊 Current Balance = {amount[name]} $")

                elif input1 == 4:
                    print("👋 Thank you for using our Bank!")
                    break
                else:
                    print("❌ Invalid option, try again.")
        else:
            print("❌ Wrong password!")
    else:
        print("❌ User not found!")

else:
    print("❌ Not valid option")
