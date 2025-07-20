class BankAccount:
        def __init__(self, accounts = None, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.accounts = accounts if accounts is not None else {}

        def all_accounts(self):
              return self.accounts
        
        def get_one_account(self, customer):
              return self.accounts(customer)