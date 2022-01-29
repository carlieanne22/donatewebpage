def show_homepage():
    print("               === DonateMe Homepage ===           ")
    print("---------------------------------------------------")
    print("| 1. Login                 | 2.    Register       |")
    print("---------------------------------------------------")
    print("| 3. Donate                | 4.    Show Donations |")
    print("---------------------------------------------------")
    print("|                        5. Exit                  |")
    print("---------------------------------------------------")

# task 6


def donate(username):
    donation_amt = float(input("Enter amount to donate: "))
    dont_string = str(donation_amt)
    donation = username, "+ donated $" + dont_string
    print("Thank you for your donation!")
    return donation


def show_donations(donations):
    print("\n--All Donations---")
    if donations == []:
        print("Currently no donations")

    else:
        for donation in donations:
            print(donation)
