# function to check the length of the word and reserves it if its 5 or more
def length_checker(word):
    if len(word) >= 5:
        return word[::-1]
    else:
        return word

# function to take a string and return it with any words longer then 5 chars reserved.
def spin_words(setence):
    word = ""
    new_setence = ""
    for char in setence:
        if char == " ":
            new_setence += length_checker(word) + " "
            word = ""
        else:
            word += char
    new_setence += length_checker(word)
    return new_setence
    
print(spin_words("Hey fellow warriors"))      