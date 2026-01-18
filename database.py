import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    password="!@**Data**1621101##@!",
    database="bank"
)

cursor = mydb.cursor()

def customerTable():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(20),
            account_number VARCHAR(30),
            password_hash VARCHAR(255),
            name VARCHAR(100),
            age INT,
            address VARCHAR(50),
            division VARCHAR(20),
            national_id BIGINT,
            dob DATE,
            status TINYINT(1)
        )
    """)
    mydb.commit()

if __name__ == "__main__":
    customerTable()

def db_querry(query, params=None):
    cursor.execute(query, params)
    result = cursor.fetchall()
    mydb.commit()
    return result


def db_execute(query, params=None):
    cursor.execute(query, params)
    mydb.commit()
