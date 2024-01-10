class BankAccount:
    def __init__(self, account_holder, account_number, balance=None):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self._validate_positive_amount(amount)
        self._initialize_balance()
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        self._validate_positive_amount(amount)
        self._initialize_balance()
        if amount > self.balance:
            print("Insufficient funds. Withdrawal canceled.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")

    def display_balance(self):
        self._initialize_balance()
        print(f"Current Balance: ${self.balance}")

    def _validate_positive_amount(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount. Please enter a positive value.")

    def _initialize_balance(self):
        if self.balance is None:
            self.balance = 0
if __name__ == "__main__":
    account1 = BankAccount("Princy", "543211234")

    account1.deposit(400)

    account1.withdraw(100)

    account1.display_balance()
            
