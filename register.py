from database import *

def SignUp():
    user_name=input("Create User name: ")
    temp=db_querry(f"SELECT username FROM customers where username ='{user_name}';")
    if temp:
        print("Username already exists.")
        SignUp()
    else:
        print("Username available, procced.")
    
