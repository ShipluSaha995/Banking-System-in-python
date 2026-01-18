from database import db_querry, db_execute
import random
import hashlib

def SignUp():
    
    while True:
        user_name = input("Create User name: ")
        if not db_querry(f"SELECT username FROM customers WHERE username='{user_name}';"):
            break
        print("Username already exists. Try again.")

    password = input("Create Password: ")
    password = hashlib.sha256(password.encode()).hexdigest()

    name = input("Name: ")
    age = int(input("Age: "))
    address = input("Address: ")
    division = input("Division: ")
    nid = int(input("National ID Number: "))
    dob = input("Date Of Birth (YYYY-MM-DD): ")

    
    while True:
        account_number = random.randint(100000000, 999999999)
        if not db_querry(
            f"SELECT account_number FROM customers WHERE account_number='{account_number}';"
        ):
            break

    db_execute(
        f"""
        INSERT INTO customers
        (username, account_number, password_hash, name, age, address, division, national_id, dob, status)
        VALUES
        ('{user_name}', '{account_number}', '{password}', '{name}', {age},
         '{address}', '{division}', {nid}, '{dob}', 1);
        """
    )

    print("Account created successfully!")
    print("Your Account Number:", account_number)




def SignIn():
    attempts = 3
    while attempts > 0:
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()

        password_hash = hashlib.sha256(password.encode()).hexdigest()

        result = db_querry(
            "SELECT * FROM customers WHERE username=%s AND password_hash=%s",
            (username, password_hash)
        )

        if result:
            print("Sign In Successful.")
            return True
        else:
            attempts -= 1
            print(f"Incorrect username or password. Attempts left: {attempts}")

    print("Login failed. Try again later.")
    return False
