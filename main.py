from register import *
from transaction import *

print("WELCOME TO THE BANK")
while True:
    try:
        register=int(input("\nEnter 1 for SingnUP and 2 for SignIn\n"
                           "1. SingnUp\n"
                           "2. SingnIn\n"
                           "3. Exit\n"
                           "Enter your choice(1/2/3): "))
        if register == 1 or register== 2 or register==3:
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
                           4. Transfer Money
                           5. Transaction History
                           6. Logout
                           
                           """
                       )
                       choice=input("Select your Choice: ")
                       if choice=="1":
                           print("Balance: ", check_balance(acc))
                       elif choice=="2":
                            deposit(acc)
                       elif choice=="3":
                           withdraw(acc)
                       elif choice=="4":
                           transfer(acc)
                       elif choice=="5":
                           history(acc)
                       elif choice=="6":
                           print("Logged out...")
                           exit()

            if register==3:
                print("Exiting...")
                exit()
                           
        else:
            print("Invalid Choice, Please give the valid input.\n")

       
    except ValueError:
        print("Invalid input Try agian.")
