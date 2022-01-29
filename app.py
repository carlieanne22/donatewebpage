from donations_pkg.homepage import show_donations, show_homepage, donate
from donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
authorized_user = ""

# while True:
show_homepage()
if authorized_user == "":
    print("You must be logged in to donate")
else:
    print("Logged in as: " + authorized_user)
while True:
    user_options = input("Choose an option: ")
# Task 3 begins
    if user_options == "1":
        username = input("Please enter username: ")
        password = int(input("Please enter password: "))
        authorized_user = login(database, username, password)
    elif user_options == "2":
        username = input("Please enter username: ")
        password = int(input("Please enter password: "))
        authorized_user = register(database, username)
        for username in database:
            if username not in database:
                database["username"] = input("Enter username:")
                database["password"] = input("Enter password")
    elif user_options == "3":
        if authorized_user == "":
            print("You must be logged in to donate")
        else:
            donation = donate(authorized_user)
    elif user_options == "4":
        show_donations(donation)

    elif user_options == "5":
        print("Goodbye..")
        break
    else:
        print("Invalid command")
# Task 3 Ends
