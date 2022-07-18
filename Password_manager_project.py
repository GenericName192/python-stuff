import DB_Connector
import password_generator_mark_two


account_list = []

def actual_program():
    service = input("What service would you like to access? please type (add) to add a new account or (view) to view an account or (view all) to view all account or finally (delete) to delete.")
    if service.upper() == "ADD":
        save_account()
    elif service.upper() == "VIEW":
        search = str(input("What account would you like to view?"))
        if view_account(search) == None:
            print("Sorry we dont seem to be able to find that account")
        else:
            print(view_account(search))
    elif service.upper() == "VIEW ALL":
        DB_Connector.Retrive_all_data()
    elif service.upper() == "DELETE":
        delete_account()
    else:
        print("It would appear somethings gone wrong, please try again")
        actual_program()
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
    generate_password = input("Would you like to have your password auto generated for you?")
    if generate_password.upper() == "YES":
        password = password_generator_mark_two.generate_password()
    else:
        password = input("What would you like the password to be?")
    DB_Connector.Save_data(website, password)



def view_account(search):
    return DB_Connector.Retrive_data(search)

def delete_account():
    website = input("What website would you like to delete the password for?")
    DB_Connector.delete_data(website)   

actual_program()