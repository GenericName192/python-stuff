from asyncio.windows_events import NULL



account_list = []

def actual_program():
    service = input("What service would you like to access? please type (add) to add a new account or (view) to view an account or (view all) to view all account.")
    if service.upper() == "ADD":
        save_account()
    elif service.upper() == "VIEW":
        search = str(input("What account would you like to view?"))
        view_account(search)
    elif service.upper() == "VIEW ALL":
        view_all_accounts()
    else:
        print("It would appear somethings gone wrong, please try again")
        actual_program
    restarter = input("Would you like to use another service? (yes) (no)")
    if restarter.upper() == "YES":
        actual_program()
    elif restarter.upper() == "NO":
        print("Have a nice day")
    else:
        print("there appears to have been an error, restarting program to be on the safe side")
        actual_program()

def save_account():
    website = input("What website would you like to store a password for?")
    password = input("What is the password?")
    make_account = [website,password]
    account_list.append(make_account)



def view_account(search):
    length = len(account_list)
    checker = 0
    while checker <= length:
        print(account_list[checker][0])
        if account_list[checker][0] == search:
            print(account_list[checker])
            break
        else:
            checker += 1
    print("Sorry it would appear you dont have an account for " + search)
    

def view_all_accounts():
    if account_list is not NULL:
        print(account_list)
    else:
        print("You dont seem to have an accounts yet, please add one and try again.")

actual_program()