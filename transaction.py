from database import db_querry, db_execute

def check_balance(account_number):
    result = db_querry(
        "SELECT balance FROM accounts WHERE account_number=%s",
        (account_number,)
    )

    if not result:
        return 0   

    return result[0][0]


def deposit(account_number):
    amount = float(input("Enter deposit amount: "))

    if amount <= 0:
        print("Invalid amount.")
        return

    
    check = db_querry(
        "SELECT account_number FROM accounts WHERE account_number=%s",
        (account_number,)
    )

    if not check:
        db_execute(
            "INSERT INTO accounts (account_number, balance) VALUES (%s, 0)",
            (account_number,)
        )

   
    db_execute(
        "UPDATE accounts SET balance = balance + %s WHERE account_number=%s",
        (amount, account_number)
    )

   
    db_execute(
        "INSERT INTO transactions (account_number, type, amount) VALUES (%s, %s, %s)",
        (account_number, "DEPOSIT", amount)
    )

    print("Deposit successful.")


def withdraw(account_number):
    amount = float(input("Withdraw Amount: "))
    balance = check_balance(account_number)

    if amount <= 0:
        print("Invalid amount.")
        return

    if amount > balance:
        print("Insufficient Balance.")
        return

    
    db_execute(
        "UPDATE accounts SET balance = balance - %s WHERE account_number = %s",
        (amount, account_number)
    )

    
    db_execute(
        "INSERT INTO transactions (account_number, type, amount) VALUES (%s, %s, %s)",
        (account_number, "WITHDRAW", amount)
    )

    print("Withdrawal successful.")



def transfer(sender):
    receiver = input("Recivers Account Number: ")
    amount = float(input("Amount: "))

    if amount <= 0:
        print("Invalid amount.")
        return

    if amount > check_balance(sender):
        print("Insufficient Balance.")
        return

   
    db_execute(
        "UPDATE accounts SET balance = balance - %s WHERE account_number = %s",
        (amount, sender)
    )

    
    db_execute(
        "UPDATE accounts SET balance = balance + %s WHERE account_number = %s",
        (amount, receiver)
    )

   
    db_execute(
        "INSERT INTO transactions (account_number, type, amount) VALUES (%s, 'TRANSFER_OUT', %s)",
        (sender, amount)
    )

    db_execute(
        "INSERT INTO transactions (account_number, type, amount) VALUES (%s, 'TRANSFER_IN', %s)",
        (receiver, amount)
    )

    print("Transfer Successful.")


def history(account_number):
    rows=db_querry(
        "SELECT type, amount, date FROM transactions WHERE account_number=%s",
        (account_number,)
    )
    for r in rows:
        print(r)