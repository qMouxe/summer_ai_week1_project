# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Login to existing account")
    print("3. Manage my account")
    print("4. Quit")
    print("5. Reset Data")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Friends")
    print("3. Mesasges")
    print("4. <- Go back ")
    return input("Please Choose a number: ")

def friendMenu():
    print("")
    print("1. Add a friend")
    print("2. View all my friends")
    print("3. View friend requests")
    print("4. Block a user")
    print("5. Unblock a user")
    return input("Please input a number: ")

def msgMenu():
    print("")
    print("1. Send a message")
    print("2. View all my messages")
    return input("Please input a number: ")