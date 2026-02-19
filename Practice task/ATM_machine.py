balance = 10000

while True:
    print("||---ATM MENU---||")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Your current balance is: {balance}")
    elif choice == 2:
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"Amount deposited successfully. New balance: {balance}")
    elif choice == 3:
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds. Please try again.")
        else:
            balance -= amount
            print(f"Amount withdrawn successfully. New balance: {balance}")