from bank_account import BankAccount
from credentials_check import AccountCredentials
from account_storage import store_details

class CreateAccount(BankAccount, AccountCredentials):
        def __init__(self, accounts = None, customer_data = None, *args, **kwargs ):
            super(). __init__(accounts = accounts, customer_data = customer_data,*args, **kwargs)

        def create_account(self):
            try:
                userid = input("Enter the User ID: ")
                userid_error = self.validate_userid(userid)
                if userid_error:
                      return "Enter a valid User ID"
            except ValueError:
                return "Invalid input! Please enter a valid User ID."

            if userid:
                try:
                    name = input("Enter the Account Holder's Full Name: ")
                    name_error = self.validate_name(name)
                    if name_error:
                      return "Enter a valid name"
                except ValueError as ve:
                    return f"An error occurred while entering the name: {ve}\nPlease enter a valid name."

                try:
                    balance = input("Enter the First Deposit Amount: ")
                    balance_error = self.validate_balance(balance)
                    if balance_error:
                      return "Enter a valid deposit."
                except ValueError:
                    return "Invalid input! Please enter numeric values for balance."
                
                try:
                    pin = input("Enter a 4-digit PIN: ")
                    pin_error = self.validate_pin(pin)
                    if pin_error:
                      return "Enter a valid PIN."
                    
                except ValueError:
                    return "Invalid input! Please enter numeric values for PIN."
            
                customer = {
                            "User ID" : userid,
                            "Name" : name,
                            "Balance" : balance,
                            "PIN" : pin         #Check later if we can store pins privately to fetch later
                        }

                if not userid in self.customer_data:
                    self.customer_data[userid] = customer
                    store_details(self.customer_data)
                else:
                      return "Welcome back sir"
                
            return f"Account created successfully: {customer}"
        
