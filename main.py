from BankManage import Bank
def main():
    bank = Bank()

    while True:
        print("====Banking Management System===")
        print('_________________________________')
        print("1. Create an user account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. Transfer")
        print("6. Take a loan")
        print("7. Transaction history")
        print("8. Admin options")
        print("9. Exit")
        print('___________________________________')

        choice = input("Enter your choice: ")

        if choice == "1":
            user_name = input("Enter your name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(user_name, initial_balance)

        elif choice == "2":
            user_name = input("Enter your name: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(user_name, amount)

        elif choice == "3":
            user_name = input("Enter your name: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(user_name, amount)

        elif choice == "4":
            user_name = input("Enter your name: ")
            bank.check_balance(user_name)

        elif choice == "5":
            sender_name = input("Enter sender's name: ")
            receiver_name = input("Enter receiver's name: ")
            amount = float(input("Enter transfer amount: "))
            bank.transfer(sender_name, receiver_name, amount)

        elif choice == "6":
            user_name = input("Enter your name: ")
            bank.take_loan(user_name)

        elif choice == "7":
            user_name = input("Enter your name: ")
            bank.transaction_history(user_name)

        elif choice == "8":
            print("\nAdmin Options")
            print("1. Check total bank balance")
            print("2. Check total loan amount")
            print("3. Off/On loan feature")
            admin_choice = input("Enter admin choice: ")
            if admin_choice == "1":
                bank.admin_check_balance()
            elif admin_choice == "2":
                bank.admin_check_loan_amount()
            elif admin_choice == "3":
                bank.admin_off_or_on_loan_feature()
            else:
                print("Invalid admin choice.")

        elif choice == "9":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
