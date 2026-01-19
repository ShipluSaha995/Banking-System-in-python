from register import *
from transaction import *

print("WELCOME TO THE BANK")
while True:
    try:
        register=int(input("\nEnter 1 for SingnUP and 2 for SignIn\n"
                           "1. SingnUp\n"
                           "2. SingnIn\n"
                           "Enter your choice(1/2): "))
        if register == 1 or register== 2:
            if register==1:
                SignUp()
            if register==2:
               acc= SignIn()
               if acc:
                   while True:
                       print(
                           """
                           1. Check Balance.
                           2. Deposit.
                           3. Withdraw. 
                           
                           
                           """
                       )
                       choice=input("Select your Choice: ")
                       if choice=="1":
                           print("Balance: ", check_balance(acc))
                       elif choice=="2":
                            deposit(acc)
                       elif choice=="3":
                           withdraw(acc)
                           
        else:
            print("Invalid Choice, Please give the valid input.\n")

        

    except ValueError:
        print("Invalid input Try agian.")
