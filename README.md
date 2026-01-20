# 🏦 Banking Management System (Python & MySQL)

A **console-based Banking Management System** built using **Python** and **MySQL** that simulates real-world banking operations such as account creation, secure login, deposits, withdrawals, money transfers, and transaction history management.

This project demonstrates **database integration**, **secure password handling**, and **modular Python programming**.

---

## 📌 Features

- **User Registration (Sign Up)** with unique usernames
- **Secure Login (Sign In)** with SHA-256 password hashing
- **Auto-generated Unique Account Numbers**
- **Check Account Balance**
- **Deposit Money**
- **Withdraw Money**
- **Transfer Money Between Accounts**
- **View Transaction History**
- **Persistent Data Storage using MySQL**
- **Modular Code Structure for easy maintenance**

---

## 🛠️ Technologies Used

- Python 3
- MySQL
- `mysql-connector-python`
- `hashlib` (for secure password hashing)
- `random` module (for account number generation)

---

## 📂 Project Structure

Banking-System/
│
├── database.py # Database connection & table creation
├── main.py # Main program & menu system
├── register.py # Sign Up & Sign In logic
├── transaction.py # Deposit, Withdraw, Transfer, and Transaction History
└── README.md # Project documentation


---

## 🗄️ Database Schema

### `customers` Table
| Column         | Type                     | Description                          |
|----------------|-------------------------|--------------------------------------|
| id             | INT (PK, Auto Increment) | Unique customer ID                    |
| username       | VARCHAR                 | Unique username                       |
| account_number | VARCHAR                 | Customer's account number             |
| password_hash  | VARCHAR                 | SHA-256 hashed password               |
| name           | VARCHAR                 | Customer's full name                  |
| age            | INT                     | Customer's age                        |
| address        | VARCHAR                 | Address                               |
| division       | VARCHAR                 | Division or state                      |
| national_id    | BIGINT                  | National ID number                     |
| dob            | DATE                    | Date of birth                          |
| contact        | VARCHAR                 | Phone number                           |
| mail           | VARCHAR                 | Email address                          |
| status         | TINYINT(1)              | Account active status (1 = active)    |

### `accounts` Table
| Column         | Type          | Description          |
|----------------|---------------|--------------------|
| account_number | VARCHAR (PK)  | Account number      |
| balance        | DOUBLE        | Current balance     |

### `transactions` Table
| Column         | Type                     | Description                                |
|----------------|--------------------------|--------------------------------------------|
| id             | INT (PK, Auto Increment) | Unique transaction ID                      |
| account_number | VARCHAR                  | Account number involved in transaction     |
| type           | VARCHAR                  | Transaction type (DEPOSIT, WITHDRAW, TRANSFER_IN/OUT) |
| amount         | DOUBLE                   | Transaction amount                          |
| date           | TIMESTAMP                | Timestamp of the transaction               |

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/banking-management-system.git
cd banking-management-system
pip install mysql-connector-python

---

# 🗄️ MySQL Workbench Commands for Banking Management System

---

## 1️⃣ Create the Database
```sql
CREATE DATABASE BANK;

## 2️⃣ Show All Databases
SHOW DATABASES;

## 3️⃣ Use the Database
SHOW DATABASES;

## 4️⃣ Show All Tables
SHOW TABLES;

## 5️⃣ View Table Data
SELECT * FROM customers;
SELECT * FROM accounts;
SELECT * FROM transactions;
