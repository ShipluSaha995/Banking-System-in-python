from database import db_querry, db_execute
import random
import hashlib

def SignUp():

    while True:
        user_name = input("Create User name: ").strip()
        if not db_querry("SELECT username FROM customers WHERE username=%s", (user_name,)):
            break
        print("Username already exists. Try again.")

    password = input("Create Password: ")
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    name = input("Name: ")
    age = int(input("Age: "))
    address = input("Address: ")
    division = input("Division: ")
    nid = int(input("National ID Number: "))
    dob = input("Date Of Birth (YYYY-MM-DD): ")
    contact = input("Contact Number: ")
    mail= input("Mail Address: ")

    while True:
        account_number = random.randint(100000000, 999999999)
        if not db_querry(
            "SELECT account_number FROM customers WHERE account_number=%s",
            (account_number,)
        ):
            break

    db_execute(
        """
        INSERT INTO customers
        (username, account_number, password_hash, name, age, address,
         division, national_id, dob, contact, mail, status)
        VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            user_name,
            account_number,
            password_hash,
            name,
            age,
            address,
            division,
            nid,
            dob,
            contact,
            mail,
            1
        )
    )

    db_execute(
        "INSERT INTO accounts (account_number, balance) VALUES (%s, 0)",
        (account_number,)
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
            "SELECT account_number FROM customers WHERE username=%s AND password_hash=%s",
            (username, password_hash)
        )

        if result:
            print("Sign In Successful.")
            return result[0][0]  
        else:
            attempts -= 1
            print(f"Incorrect username or password. Attempts left: {attempts}")

    return None
