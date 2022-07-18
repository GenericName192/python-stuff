#there is no actual change but it thinks there is one so you get a comment.
user_list = []
import random
import string
password_max_length = 10
def actual_program_manager():
    account_tracker = len(user_list)
    user_name = new_user()
    password = generate_password()
    account_tracker = create_user(user_name, password, account_tracker)
    run_again = input("Would you like to create another user? (yes) (no)").upper()
    if run_again == "YES":
        actual_program_manager()

def new_user():
    user_name = input("What would you like your username to be?")
    password = []
    password_current_length = 0
    return user_name

def generate_password():
    special_chars = ["!", "£", "$", "%", "^", "&", "*", "(", ")", ":", ";", "?"]
    password = []
    password_current_length = 0
    while password_current_length <= password_max_length:
        char_picker = random.randint(0,2)
        if char_picker == 0:
            temp_char = random.choice(string.ascii_letters)
            temp_number = random.randint(0,1)
            if temp_number == 0:
                password.append(temp_char)
                password_current_length += 1
            else:
                password.append(temp_char.upper())
                password_current_length += 1
        elif char_picker == 1:
            password.append(str(random.randint(0,9)))
            password_current_length += 1
        elif char_picker == 2:
            temp_number = random.randint(0,11)
            password.append(special_chars[temp_number])
            password_current_length += 1
        else:
            print("Well this is awkward this shouldnt have happened.")

    return "".join(password)

def create_user(user_name, password, account_tracker):
    account = [user_name, password]
    user_list.append(account)
    print("This is your new account, "+ ": ".join(account) + " make sure to rememeber is as im not sure how to recover the password yet =D and your account number is ", account_tracker)
    return account_tracker +1

actual_program_manager()