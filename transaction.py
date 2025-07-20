from account_storage import load_json
from utils import get_amount

@staticmethod
def transaction(userid):
     data = load_json()
     src_acc = input("Enter the User ID you want to transfer money from: ").zfill(2)
     dst_acc = input("Enter the User ID you want to transfer money to: ").zfill(2)

     if src_acc not in data:
                print("Source User ID doesn't exists!")
                
     if dst_acc not in data:
         print("Destination User ID doesn't exists!")
         return
            
     amount = get_amount()
     src_balance = float(data[src_acc]['Balance'])
     dst_balance = float(data[dst_acc]['Balance'])

     if src_balance < amount:
         return f"Insufficient balance in {src_balance}"
     
     src_balance -= amount
     dst_balance += amount

     data[src_acc]['Balance'] = str(src_balance)
     data[dst_acc]['Balance'] = str(dst_balance)

     print(f"\nSuccessfully transferred ₹{amount} from {data[src_acc]['Name']} to {data[dst_acc]['Name']}.")
     print(f"New Balance - {data[src_acc]['Name']}: ₹{data[src_acc]['Balance']}")
     print(f"New Balance - {data[dst_acc]['Name']}: ₹{data[dst_acc]['Balance']}")