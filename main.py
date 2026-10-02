accounts = {}


def create_account():
    name = input("Enter your name: ")
    account_number = input("Enter account number: ")
    pin = input("Set your PIN: ")

    accounts[account_number] = {
        "name": name,
        "pin": pin,
        "balance": 0
    }

    print("Account created successfully!")


def login():
    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")

    if account_number in accounts and accounts[account_number]["pin"] == pin:
        print("Login successful!")
        return account_number

    print("Invalid account number or PIN.")
    return None


def deposit(account_number):
    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        accounts[account_number]["balance"] += amount
        print("Amount deposited successfully!")
        print("Current balance:", accounts[account_number]["balance"])
    else:
        print("Invalid amount.")


def withdraw(account_number):
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount.")
    elif amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
    else:
        accounts[account_number]["balance"] -= amount
        print("Amount withdrawn successfully!")
        print("Current balance:", accounts[account_number]["balance"])
        
def transfer(account_number):
    receiver = input("Enter receiver account number: ")
    amount = float(input("Enter transfer amount: "))

    if receiver not in accounts:
        print("Receiver account not found.")
    elif amount <= 0:
        print("Invalid amount.")
    elif amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
    else:
        accounts[account_number]["balance"] -= amount
        accounts[receiver]["balance"] += amount

        print("Amount transferred successfully!")
        print("Current balance:", accounts[account_number]["balance"])


def check_balance(account_number):
    print("Current balance:", accounts[account_number]["balance"])


def main():
    while True:
        print("\n===== PYTHON BANKING APP =====")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            account_number = login()

            if account_number:
                while True:
                    print("\n===== ACCOUNT MENU =====")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Transfer")
                    print("5. Logout")

                    option = input("Enter your choice: ")

                    if option == "1":
                        deposit(account_number)

                    elif option == "2":
                        withdraw(account_number)

                    elif option == "3":
                        check_balance(account_number)
                        
                    elif option == "4":
                        transfer(account_number)

                    elif option == "5":
                        print("Logged out successfully.")
                        break

                    else:
                        print("Invalid choice.")

        elif choice == "3":
            print("Thank you for using the banking app!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()