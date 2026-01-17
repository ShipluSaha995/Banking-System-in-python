print("WELCOME TO THE BANK")
while True:
    try:
        register=int(input("\nEnter 1 for SingnUP and 2 for SignIn\n"
                           "1. SingnUp\n"
                           "2. SingnIn\n"
                           "Enter your choice(1/2): "))
        if register == 1 or register== 2:
            pass
        else:
            print("Invalid Choice, Please give the valid input.\n")

    except ValueError:
        print("Invalid input Try agian.")
