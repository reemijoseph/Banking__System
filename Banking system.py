class BankAccount:
    def _init_(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def login(self, entered_pin):
        if entered_pin == self.pin:
            print("Login successful!")
            return True
        else:
            print("Incorrect PIN. Login failed.")
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Account Balance: ${self.balance}")


def main():

    account_number = input("Enter your account number: ")

    while True:
        pin = input("Create a 4-digit PIN: ")
        if pin.isdigit() and len(pin) == 4:
             break
        else:
            print("Invalid PIN. Please enter a 4-digit number.")

    user_account = BankAccount(account_number,pin)
    entered_pin = input("Enter your PIN to login: ")
    if user_account.login(entered_pin):
      while True:
            print("\n options:")
            print("1: deposit")
            print("2: withdrawal")
            print("3: balance")
            print("4: exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                amount = float(input("Enter the amount to deposit: "))
                user_account.deposit(amount)

            elif choice == '2':
                amount = float(input("Enter the amount to withdraw: "))
                user_account.withdraw(amount)

            elif choice == '3':
                user_account.check_balance()

            elif choice == '4':
                print("Exiting the banking system. Thank you!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "_main_":
    main()