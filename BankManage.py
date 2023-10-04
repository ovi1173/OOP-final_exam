class Bank:
    def __init__(self):
        self.users = {}  
        self.bank_balance = 0
        self.loan_feature = True
        self.total_loan_amount = 0


    def create_account(self, user_name, initial_balance):
        if user_name in self.users:
            print("Account already exists.")
        else:
            self.users[user_name] = initial_balance
            self.bank_balance += initial_balance
            print(f"Account created for {user_name} with an initial balance of {initial_balance}")

    def deposit(self, user_name, amount):
        if user_name in self.users:
            self.users[user_name] += amount
            self.bank_balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Account not found.")

    def withdraw(self, user_name, amount):
        if user_name in self.users:
            if self.users[user_name] >= amount:
                self.users[user_name] -= amount
                self.bank_balance -= amount
                print(f"{amount} withdrawn successfully.")
            elif self.bank_balance < amount:
                print("The bank is bankrupt!!")
            else:
                print("insufficient balance!!")
        else:
            print("Account not found.")

    def check_balance(self, user_name):
        if user_name in self.users:
            print(f"Available balance for {user_name}: {self.users[user_name]}")
        else:
            print("Account not found.")

    def transfer(self, sender_name, receiver_name, amount):
        if sender_name in self.users and receiver_name in self.users:
            if self.users[sender_name] >= amount:
                self.users[sender_name] -= amount
                self.users[receiver_name] += amount
                print(f"{amount} transferred from {sender_name} to {receiver_name} successfully.")
            else:
                print("Insufficient balance. Transfer failed.")
        else:
            print("Account not found.")

    def transaction_history(self, user_name):
        if user_name in self.users:
            print(f"Transaction history for {user_name}:")
           
        else:
            print("Account not found.")

    def take_loan(self, user_name):
        if self.loan_feature:
            if user_name in self.users:
                loan_amount = 2 * self.users[user_name]
                self.users[user_name] += loan_amount
                self.total_loan_amount += loan_amount
                print(f"{loan_amount} loan granted to {user_name}.")
            else:
                print("Account not found.")
        else:
            print("Loan feature is currently turned off.")

    def admin_check_balance(self):
        print(f"Total available balance in the bank: {self.bank_balance}")

    def admin_check_loan_amount(self):
        print(f"Total loan amount granted by the bank: {self.total_loan_amount}")

    def admin_off_or_on_loan_feature(self):
        self.loan_feature = not self.loan_feature
        status = "ON" if self.loan_feature else "OFF"
        print(f"Loan feature is now {status}")

