import utility
class Bank_Account():
    def _init_(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password
        self.user_balance = 5000

    def deposit(self, amount):
        self.user_balance += amount
        print(f"Amount {amount} deposited successfully.")

    def withdraw(self, amount):
        if self.user_balance - amount >= 5000:
            self.user_balance -= amount
            print(f"Amount {amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

class Secure_Bank_Account(Bank_Account):
    def check_user_authentication(self, user_name, user_password):
        if (user_password == self.user_password) and (user_name == self.user_name):
            return True
        else:
            return False

    def display_balance(self):
        print(f"User Name: {self.user_name}")
        print(f"Current Balance: {self.user_balance}")

account = Secure_Bank_Account("Yug", "Password")
max_attempts = int(input("Enter attempts : "))
attempts = 0

while attempts < max_attempts:
    input_user_name = input("Enter the user_name: ")
    input_user_password = input("Enter the Password : ")
    ac2 = account.check_user_authentication(input_user_name, input_user_password)
    if ac2:
        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Display Balance\n4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                a = utility.check_num_positive(amount)
                if a == 1:
                    account.deposit(amount)
                else:
                    print("invalid amount")
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                a = utility.check_num_positive(amount)
                if a == 0:
                    print("invalid amount")
                else:
                    account.withdraw(amount)
            elif choice == '3':
                account.display_balance()
            elif choice == '4':
                print("Thank you for banking with us!")
                exit()  
            else:
                print("Invalid choice. Please enter a valid option.")
    else:
        attempts += 1
        print(f"Incorrect Password or User Name. Attempts Left : {max_attempts - attempts}")
print("Too many incorrect attempts. Exiting...")