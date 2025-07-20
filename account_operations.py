import json
from account_storage import load_json
from utils import get_amount

class Account:
        def __init__(self, userid, name, pin, balance=0):
            self.userid = userid
            self.name = name
            self.balance = balance
            self.pin = pin
        
        @staticmethod
        def login():
            userid = input("Enter your USER ID: ")
            pin = input("Enter your PIN Number: ")
            data = load_json()

            if userid in data and str(data[userid]["PIN"]) == pin:
                print(f"\n\tLOGIN SUCCESSFUL!\nUser ID: {userid}")
                return userid
            else:
                return "INVALID CREDENTIALS"
            
        @staticmethod
        def display_account(userid):
            try:
                with open('customer_data.json', 'r') as f:
                    data = json.load(f)
                    if userid not in data:
                        print(f"User ID {userid} not found in data.")
                        return
                    
                    user_info = data[userid]
                    print(f"\nAccount details for User ID: {userid}")
                    for key,values in user_info.items():
                        print(f"{key.capitalize()}: {values}")

            except json.JSONDecodeError:
                return "File present is empty or currupted."
            except FileNotFoundError:
                print("Error: customer_data.json file not found.")

        @staticmethod
        def deposit(userid):
            data = load_json()
            amount = get_amount()
            data[userid]['Balance'] = str(float(data[userid]['Balance']) + amount)

            with open('customer_data.json', 'w') as f:
                json.dump(data, f, indent=4)
                print(f"Deposited {amount} to {data[userid]['Name']}'s account.\nCurrent Balance: {data[userid]['Balance']}")

        @staticmethod
        def withdraw(userid):
            data = load_json()
            amount = get_amount()
            data[userid]['Balance'] = str(float(data[userid]['Balance']) - amount)

            with open('customer_data.json', 'w') as f:
                json.dump(data, f, indent=4)
                print(f"Withdrawed {amount} to {data[userid]['Name']}'s account.\nCurrent Balance: {data[userid]['Balance']}")


