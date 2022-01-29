# task 4
def login(database, username, password):
    if username in database:
        if database[username] == password:
            print("Welcome back! ")
            return username
        elif database[username] != password:
            print("Incorrect password for admin.")
            return ""
        else:
            if username not in database:
                print("User not found. Please register. ")
                return ""


# task 5
def register(database, username):
    if username in database:
        print("Username already registered")
        return ""
    else:
        if username not in database:
            print("Username confirmed")
            return username
