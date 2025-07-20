from bank_account import BankAccount
from credentials_check import AccountCredentials
from account_operations import Account
from create_account import CreateAccount
from account_storage import store_details , load_json
from transaction import transaction

def main():
    print("\t\t\tWelcome to the BANK ACCOUNT MANAGEMENT SERVICES")
    bank = BankAccount()
    customer_data = load_json()

    creator = CreateAccount(accounts = bank.accounts, customer_data = customer_data)

    while True:
        print("\nPRESS:")
        print("\'1\'Create New Account")
        print("\'2\'Account Operations")
        print("\'3\'exit")

        try:
            choice = input("\nEnter your choice: ")
        except ValueError:
            return "Choice entered must be in numeric form!"

        if len(choice) != 1:
            return "Enter a valid choice (1,2,3)"
        else:
            if choice in ['1']:
                acc = CreateAccount()
                acc.create_account()
                    
            elif choice in ['2']:
                userid = Account.login()
                if userid in customer_data:
                    while True:
                        print("\n\'1\' to Display Account INFO.")
                        print("\'2\' to Make a Deposit.")
                        print("\'3\' to Make a Withdrawal.")
                        print("\'4\' to Make a Transaction.")
                        print("\'5\' to LogOut\n")

                        op = input("\nEnter the Operation you want to perform: ")

                        if op == '1':
                            Account.display_account(userid)
                        elif op == '2':
                            Account.deposit(userid)
                        elif op == '3':
                            Account.withdraw(userid)
                        elif op =='4':
                            transaction(userid)
                        elif op =='5':
                            break
                        else:
                            return "Enter a valid operation."
                        
            elif choice in ['3']:
                exit("\n\t\t\tThanks for using Bank Management System")
            
            else:
                return "Enter a valid choice"
 
    
if __name__ == "__main__":
    main()