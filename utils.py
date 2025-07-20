def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                print("Amount must be positive and greater then zero")
            else:
                return amount
        except ValueError:
            print("INVALID INPUT! Enter a numeric value.")