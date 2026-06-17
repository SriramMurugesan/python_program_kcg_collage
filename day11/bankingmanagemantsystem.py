import json
from abc import ABC, abstractmethod

FILE_NAME = "accounts.json"

def load_data():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


class BankAccount(ABC):
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance   

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit amount")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount

    @abstractmethod
    def add_interest(self):
        pass


class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self.get_balance() * 0.04
        self.set_balance(self.get_balance() + interest)


class CurrentAccount(BankAccount):
    def add_interest(self):
        print("No interest for Current Account")


class BankSystem:
    def __init__(self):
        self.accounts = load_data()  
        self.deleted_accounts = set() 

    def create_account(self):
        try:
            acc_no = input("Enter Account Number: ")
            name = input("Enter Name: ")
            balance = float(input("Enter Initial Balance: "))
            acc_type = input("Savings / Current: ").lower()

            account_data = (name, balance)

            if acc_type == "savings":
                acc = SavingsAccount(acc_no, *account_data)
            else:
                acc = CurrentAccount(acc_no, *account_data)

            self.accounts[acc_no] = {
                "name": acc.name,
                "balance": acc.get_balance(),
                "type": acc_type
            }

            save_data(self.accounts)
            print(" Account Created")

        except Exception as e:
            print("Error:", e)

    def deposit(self):
        try:
            acc_no = input("Enter Account Number: ")
            amount = float(input("Enter Amount: "))

            acc = self.accounts[acc_no]
            acc["balance"] += amount

            save_data(self.accounts)
            print("Deposited")

        except Exception as e:
            print("Error:", e)

    def withdraw(self):
        try:
            acc_no = input("Enter Account Number: ")
            amount = float(input("Enter Amount: "))

            if self.accounts[acc_no]["balance"] < amount:
                raise ValueError("Insufficient Balance")

            self.accounts[acc_no]["balance"] -= amount

            save_data(self.accounts)
            print("Withdrawn")

        except Exception as e:
            print("Error:", e)

    def add_interest(self):
        try:
            acc_no = input("Enter Account Number: ")
            acc = self.accounts[acc_no]

            if acc["type"] == "savings":
                interest = acc["balance"] * 0.04
                acc["balance"] += interest
                print("Interest Added")
            else:
                print("No interest for current account")

            save_data(self.accounts)

        except Exception as e:
            print("Error:", e)

    def view_account(self):
        try:
            acc_no = input("Enter Account Number: ")
            acc = self.accounts[acc_no]

            print("\n--- Account Details ---")
            print("Name:", acc["name"])
            print("Balance:", acc["balance"])
            print("Type:", acc["type"])

        except Exception as e:
            print("Error:", e)

    def view_all_accounts(self):
        print("\n--- All Accounts ---")
        for acc_no, acc in self.accounts.items():
            print(acc_no, acc)

    def delete_account(self):
        try:
            acc_no = input("Enter Account Number: ")
            self.deleted_accounts.add(acc_no)  # set usage
            del self.accounts[acc_no]

            save_data(self.accounts)
            print("🗑️ Account Deleted")

        except Exception as e:
            print("Error:", e)


def main():
    bank = BankSystem()

    while True:
        print("""
1. Create Account
2. Deposit
3. Withdraw
4. Add Interest
5. View Account
6. View All Accounts
7. Delete Account
8. Exit
""")

        choice = input("Enter choice: ")

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.deposit()
        elif choice == "3":
            bank.withdraw()
        elif choice == "4":
            bank.add_interest()
        elif choice == "5":
            bank.view_account()
        elif choice == "6":
            bank.view_all_accounts()
        elif choice == "7":
            bank.delete_account()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()