#just the actual password generation part from my password_generator_project, not sure why i called it mark two i just didnt know what to call it.
import random
import string
password_max_length = 10
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