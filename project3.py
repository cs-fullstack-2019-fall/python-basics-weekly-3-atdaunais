# set global variables to use in the main while loop
# before the loop executes, the program will ask for the user's name and PIN. These will be used throughout the program
mainMenu = ""
total_balance = 0
userName = input("What is the name on this account?\n")
userPIN = input("Enter your 4 digit PIN: ")

while mainMenu != "4":  # sets a negative condition for the while loop to break
    # main menu displays on several lines and uses input to bring user down to the if cases
    mainMenu = input(f"Hello {userName}! Please choose one of following options:\n"
                     f"1) Check balance\n2) Add money to account\n"
                     f"3) Withdraw money from account\n4) Quit\nWhat would you like to do?\n")

    if mainMenu == "1":  # displays user's total at any time throughout the loop. starts at 0
        print(f"\n{userName}'s balance is currently: ${total_balance}\n")

    elif mainMenu == "2":  # adds funds to the total balance global variable and displays them in a print message
        add_money = int(input(f"How much money would {userName} like to deposit?\n"))
        total_balance += add_money
        print(f"{userName}'s account now holds: ${total_balance}\n")

    elif mainMenu == "3":  # removes funds from total balance global variable and displays new total after verifying PIN
        checkPIN = input(f"Please verify {userName}'s PIN: ")
        if checkPIN == userPIN:
            withdrawal = int(input(f"How much would {userName} like to withdraw?\n"))
            if withdrawal > total_balance:  # checks to see if user attempts to take more money than they have
                print("Insufficient funds\n")
            else:
                total_balance -= withdrawal  # adds user input to the total amount
                print(f"{userName}'s total balance is now: ${total_balance}\n")
        else:
            print("INVALID PIN\n")  # Error message for incorrect PIN input

    elif mainMenu == "4":  # sends a goodbye message when user chooses the quit option on main menu
        print("Goodbye!")