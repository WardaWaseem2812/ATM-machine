class ATM:
    def __init__(self):
        self.balance = 5000.0
        self.pin = "1234"
        self.authenticated = False

    def __str__(self):
        status = "Authenticated" if self.authenticated else "Not Authenticated"
        return f"<ATM | Balance: ₹{self.balance}, Status: {status}>"
    
    def check_pin(self, input_pin):
        if input_pin == self.pin:
            self.authenticated = True
            print("PIN verified successfully.")
        else:
            self.authenticated = False
            print("Invalid PIN.")

    def check_balance(self):
        if not self.authenticated:
            print("Access denied. Please verify your PIN first.")
        else:
            print(f"Your current balance is Rs. {self.balance}.")

    def deposit(self, amount):
        if not self.authenticated:
            print("Access denied. Please verify your PIN first.")
        elif amount <= 0:
            print("Invalid deposit amount. Must be greater than zero.")
        else:
            self.balance += amount
            print(f"Deposited Rs. {amount}. New balance is Rs. {self.balance}.")

    def withdraw(self, amount):
        if not self.authenticated:
            print("Access denied. Please verify your PIN first.")
        elif amount <= 0:
            print("Invalid withdrawal amount. Must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew Rs. {amount}. Remaining balance is Rs. {self.balance}.")

    def exit(self):
        print("Thank you for using the ATM. Goodbye!")
        exit()

    def menu(self):
        print("=== Welcome to the ATM menu ===")
        attempts = 0
        while attempts<3:
            input_pin = input("Enter your 4-digit pin number: ")
            if input_pin == self.pin:
                self.authenticated = True
                print("PIN verified successfully.")
                break
            else:
                attempts += 1
                print(f"Invalid PIN. Attempts left: {3 - attempts}.")
        else:
            print("Too many incorrect attempts. Exiting the menu.")
            return
        
        
        while True:
            print("==== ATM Menu ====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("Select an option (1-4): ")

            if choice == '1':
                atm.check_balance()
            elif choice == '2':
                try:
                    amount = float(input("Enter amount to deposit: "))
                    atm.deposit(amount)
                except ValueError:
                    print("Invalid input. Amount must be a number.")
            elif choice == '3':
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    atm.withdraw(amount)
                except ValueError:
                    print("Invalid input. Amount must be a number.")
            elif choice == '4':
                atm.exit()
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    atm = ATM()
    atm.menu()
