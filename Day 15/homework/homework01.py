# Creating a while loop that continuously asks the user to enter a password until they input the correct password "Goa best", 
# and printing the count of incorrect passwords.

password = "Goa best"
incorrect_password_count = 0

while True:
    entered_password = input("Enter a password: ")

    if entered_password != password:
        incorrect_password_count += 1
        print("Incorrect password count = ", incorrect_password_count)
        
    else:
        print("Correct password.   Total incorrect passwords typed:", incorrect_password_count)
        break
