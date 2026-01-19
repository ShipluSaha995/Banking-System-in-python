from database import db_querry, db_execute

def chrck_balance(account_number):
    result=db_querry(
        "SELECT bslance FROM accounts WHERE account_number=%s",
        (account_number),
    )
    return result [0][0]

def deposit(account_number):
    amount=float(input("Enter Amount: "))
    db_execute(
        "UPDATE accounts SET balance = balance + %s WHERE account_number=%s",
        (amount), (account_number)
    )
    db_execute(
        "INSERT INTO transactions (account_number, type, amount) VALUES (%s, 'DEPOSIT', %s)",
        (account_number, amount)
    )
    print("Deposit Successfull")