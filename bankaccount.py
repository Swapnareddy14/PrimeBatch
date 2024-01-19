class BankAccount:
    def __init__(self, account_holder_name, account_number, balance=0.0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
            else:
                print("Insufficient funds. Withdrawal not allowed.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")


# Example Usage:

# Create a new bank account
account1 = BankAccount("John Doe", "1234567890")

# Display initial balance
account1.display_balance()

# Deposit money
account1.deposit(1000)

# Withdraw money
account1.withdraw(500)

# Display updated balance
account1.display_balance()
