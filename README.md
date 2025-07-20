
# 🏦 Bank Management System (Python Console App)

A simple console-based Bank Management System built in Python using object-oriented programming. The system handles basic banking operations like viewing account details, depositing, withdrawing, and transferring money between users — all stored in a local JSON file.

---

## 📁 Project Structure

Bank Management/
├── main.py               # Entry point for the program
├── account_operations.py # Contains banking operations (deposit, withdraw, transaction)
├── account_storage.py    # Handles loading/saving JSON data
├── bank_account.py       # Manages account class definitions
├── utils.py              # Utility functions like input validations
├── customer_data.json    # Stores all user account data
└── README.md             # Project documentation


---

## 🚀 Features

- ✅ View account details  
- 💰 Deposit money to any account  
- 💸 Withdraw money securely  
- 🔁 Transfer funds from one user to another  
- 🧾 JSON file as persistent storage  
- 🔐 PIN-based access for basic authentication  

---

## 🧪 Sample Data (JSON)

json
{
  "01": {
    "User ID": "01",
    "Name": "Yoganshu Sharma",
    "Balance": "50000",
    "PIN": "9990"
  },
  "02": {
    "User ID": "02",
    "Name": "Deepak Sharma",
    "Balance": "9000000",
    "PIN": "9786"
  }
}


---

## 🔧 Requirements

- Python 3.6+
- No external libraries required (uses built-in `json` and `os`)

---

## 🛠 How to Run

Clone the repo:

bash
git clone https://github.com/yourusername/bank-management.git
cd bank-management


Run the program:

bash
python main.py


---

## 🧠 How It Works

Each user has:

- A unique **User ID**
- A **PIN** for login
- A **Balance** stored as a string in JSON

All operations load the latest data from `customer_data.json`, update the records, and save them back — ensuring data persistence.

A balance stored as a string in JSON# 🏦 Bank Management System (Python Console App)

A simple console-based Bank Management System built in Python using object-oriented programming. The system handles basic banking operations like viewing account details, depositing, withdrawing, and transferring money between users — all stored in a local JSON file.

---

## 📁 Project Structure

Bank Management/
├── main.py # Entry point for the program
├── account_operations.py # Contains banking operations (deposit, withdraw, transaction)
├── account_storage.py # Handles loading/saving JSON data
├── bank_account.py # Manages account class definitions
├── utils.py # Utility functions like input validations
├── customer_data.json # Stores all user account data
└── README.md # Project documentation

pgsql
Copy
Edit

---

## 🚀 Features

- ✅ View account details  
- 💰 Deposit money to any account  
- 💸 Withdraw money securely  
- 🔁 Transfer funds from one user to another  
- 🧾 JSON file as persistent storage  
- 🔐 PIN-based access for basic authentication  

---

## 🧪 Sample Data (JSON)

```json
{
  "01": {
    "User ID": "01",
    "Name": "Yoganshu Sharma",
    "Balance": "50000",
    "PIN": "9990"
  },
  "02": {
    "User ID": "02",
    "Name": "Deepak Sharma",
    "Balance": "9000000",
    "PIN": "9786"
  }
}
```
🔧 Requirements
Python 3.6+

No external libraries required (uses built-in json and os)

🛠 How to Run
Clone the repo:

bash
Copy
Edit
git clone https://github.com/yourusername/bank-management.git
cd bank-management
Run the program:

bash
Copy
Edit
python main.py
🧠 How It Works
Each user has:

A unique User ID

A PIN for login

A Balance stored as a string in JSON

## 📌 Notes

- Ensure the `customer_data.json` file is not empty or corrupted.
- Avoid using the same User ID for both source and destination in a transaction.
- Balance is stored as string to keep consistency in JSON formatting.

---

## 🧑‍💻 Author

**Yoganshu Sharma**

Feel free to ⭐ star the repo, 🛠 contribute, or 🍴 fork it!

<<<<<<< HEAD
📄 License
This project is licensed under the MIT License.

vbnet
Copy
Edit

✅ You can copy-paste this into your `README.md` and it will appear perfectly on GitHub.


All operations load the latest data from customer_data.json, update the records, and save them back — ensuring data persistence.

📌 Notes
Ensure the customer_data.json file is not empty or corrupted.

Avoid using the same User ID for both source and destination in a transaction.

Balance is stored as string to keep consistency in JSON formatting.

🧑‍💻 Author
Yoganshu Sharma

Feel free to ⭐ star the repo, 🛠 contribute, or 🍴 fork it!

📄 License
This project is licensed under the MIT License.
=======
---

## 📄 License

ThiUpdate README.md)s project is licensed under the **MIT License**.
