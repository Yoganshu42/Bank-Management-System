class AccountCredentials:
        def __init__(self, customer_data = None, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.customer_data = customer_data if customer_data is not None else {}

        def validate_userid(self,userid):
            if userid in self.accounts:
                return "User ID already exists. Please try a different one."
            else: 
                if not userid.strip():
                        raise ValueError("Account cannot be empty.")
                elif not userid.isdigit():
                        raise ValueError("User ID can only contain Numbers.")
                elif len(userid) < 2:
                        return "User ID cannot be less than 2 characters"
                elif len(userid) > 50:
                        return "User ID cannot be more than 50 characters"
             
        def validate_name(self,name):
            if not name.strip():
                        raise ValueError("Name cannot be empty.")
            elif not all(char.isalpha() or char.isspace() for char in name):
                        raise ValueError("Name can only contain numbers.")
            elif len(name) < 3:
                        return "Name must be at least 3 characters long."
            elif len(name) > 50:
                        return "Name must not exceed 50 characters."

        def validate_balance(self,balance):
            if not balance != 0:
                        raise ValueError("Account cannot be empty.")
            elif not balance.isdigit():
                        raise ValueError("Balance can only contain numbers.")
            elif len(balance) < 3:
                        return "Enter a valid deposit amount"
            elif len(balance) > 15:
                        return "Enter a valid deposit amount"
            
        def validate_pin(self,pin):
            if not pin.strip():
                        raise ValueError("Pin cannot be empty.")
            elif not pin.isdigit():
                        raise ValueError("PIN Number can only contain numbers.")
            elif len(str(pin)) != 4:
                        return "Pin must be of 4 digits"
