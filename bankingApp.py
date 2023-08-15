class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        new_username = len(new_name)
        if new_username < 2 or new_username > 10:
            print("Request denied.\nUser name must be between 2-10 characters.")
            return False
        self.name = new_name

    def change_pin(self, new_pin):
        if len(str(new_pin)) != 4:
            print("Request denied.\nPin must be four numbers.")
            return False
        self.pin = new_pin

    def change_password(self, new_password):
        if len(new_password) <= 5:
            print("Request denied.\nPassword must be more than 5 characters.")
            return False
        
        self.password = new_password



class BankUser(User): 
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
    
    def show_balance(self):
        print(self.name+ "'s balance: $"+ "{:.2f}".format(self.balance))
    
    def withdraw(self, withdraw_amount):
        if self.balance - withdraw_amount < 0:
            print("Insufficient funds.\nTransaction cancelled.")
            return False
        
        self.balance -= withdraw_amount
        print("${:.2f}".format(withdraw_amount),"has been withdrawn from", self.name+".")
    
    def deposit(self, deposit_amount):
        if isinstance(deposit_amount, str) or deposit_amount <= 0:
            print("Deposit amount must be a numeric value greater than $0.")
            return False      
        
        self.balance += deposit_amount
        print("${:.2f}".format(deposit_amount), "has been deposited to", self.name+"'s account.")

    def transfer_money(self, other_user):
        pin_code = int(input("User authentication required.\nEnter your pin to transfer funds: "))
        if pin_code != self.pin:
            print("Incorrect pin.\nTransaction cancelled.")
            return False
        transfer_amount = float(input("Enter amount to transfer: "))
        if self.balance - transfer_amount < 0:
            print("Insufficient funds.\nTransaction cancelled.")
            return False
       
        self.balance -= transfer_amount
        other_user.balance += transfer_amount
        print("Transfer successful.")

    def request_money(self, requested_amount, other_user):
        amount_after_transfer = other_user.balance - requested_amount
        if amount_after_transfer < 0:
            print("Insufficient funds.\nTransaction cancelled.")
            return False
        
        print(f"You are requesting ${requested_amount} from {other_user.name}")
        pin = input(f"User authentication required.\nEnter {other_user.name}'s pin: ") 
        
        if int(pin) != other_user.pin:
            print("Invalid pin. Transfer not authorized.")
            return False
        
        enter_your_password = input("Please enter your password: ")
        if enter_your_password != self.password:
            print("Invalid password. Transfer not authorized.")
            return False
        
        print("Transfer request authorized.")
        other_user.balance -= requested_amount
        self.balance += requested_amount
        return True

# Test code for bankingApp


# # Driver code for task 1
test_user1 = User("Bob", 1234, "password")
print(test_user1.name, test_user1.pin, test_user1.password)


# # Driver code for task 2
# test_user1 = User("Bob", 1234, "password1")
# print(test_user1.name, test_user1.pin, test_user1.password)
# test_user1.change_name("Daniel")
# test_user1.change_pin(4321)
# test_user1.change_password("password2")
# print(test_user1.name, test_user1.pin, test_user1.password)

# # Driver code for task 3
# test_user1 = BankUser("Bob", 1234, "password1")
# print(test_user1.name, test_user1.pin, test_user1.password, test_user1.balance)


# # Driver code for task 4
# test_user1 = BankUser("Bob", 1234, "password1")
# test_user1.show_balance()
# test_user1.deposit(1000.57)
# test_user1.show_balance()
# test_user1.withdraw(500)
# test_user1.show_balance()

# Driver code for task 5
# test_user1 = BankUser("Daniel", 1234, "password1")
# test_user2 = BankUser("Ezra", 4321, "password2")


# test_user2.deposit(5000)
# test_user2.show_balance()
# test_user1.show_balance()
# print('')
# test_user2.transfer_money(test_user1)
# test_user2.show_balance()
# test_user1.show_balance()
# print('')
# test_user2.request_money(200, test_user1)
# test_user2.show_balance()
# test_user1.show_balance()

# Bonus task 1
# test_user1 = BankUser("Daniel", 1234, "password1")

# test_user1.deposit(100)
# test_user1.show_balance()

# Bonus task 2 
# test_user1 = BankUser("Daniel", 1234, "password1")
# test_user2 = BankUser("Ezra", 4321, "password2")

# Bonus task 3: 
# test_user1 = BankUser("Daniel", 1234, "password1")
# test_user1.change_name("Danielsonny")
# test_user1.change_password("D")
# test_user1.change_pin(1)
# print(test_user1.name)

# Bonus task 4
# test_user1 = BankUser("Daniel", 1234, "password1")
# test_user1.show_balance()

# Bonus task 5




