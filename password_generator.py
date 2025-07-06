dictonary={'emma':111,
           'bella':222,
           'anna':333,}

while True:

    ask=input("would you like to 1. add a new user or 2. new user/password or would you like to LOG IN to your existing account: ")

    if ask=="1":
        name=input("what do you want your new username to be: ")
        password=input("what would you like your password to be: ")
        dictonary[name]=password

    elif ask=="2":
        user=input("what is your username: ")
        if user in dictonary:
            pas=input("what is the password: ")
            if dictonary[user]==pas:
                print("you are now logged in")
                break
            else:
                print("your password is not valid, try again")
        else:
            print("invalid user, plese try again")
    else:
        print("that is not a valid answer, please type 1 or 2")