# writing a program that simulates basic ATM

PIN = 3333
balance = 2000

while True:
    PIN = int(input("Enter PIN: "))

    if PIN != 3333:
        print("Wrong PIN, try again: ")
    else:
        fill = int(input("How much money would you like to add to your bank account: "))
        balance += fill

        print("Operation successfully completed. Your balance is now $", balance)
        while True:
            answer1 = input("Do you want to withdraw money from your bank account (Please answer with yes or no): ")

            if answer1 == "no":
                print("End of operation")
                exit()
            elif answer1 != "no" and answer1 != "yes":
                print("Invalid input, please enter 'yes' or 'no'")
            else:
                while True:
                    answer2 = int(input("How much money do you want to withdraw from your bank account: "))

                    if answer2 > balance:
                        print("you don't have enough money in your bank account, try less!")
                    elif answer2 <= balance:
                        balance -= answer2
                        
                        print("Operation successfully completed. Your balance is now $", balance) 
                        exit()