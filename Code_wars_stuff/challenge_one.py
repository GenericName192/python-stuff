# funcetion to take a number and return only the last for chars.
def maskify(cc):

    endstring = cc[-4:]
    newstring = ""
    for x in range(len(cc) - 4):
        newstring = newstring + "#"

    return newstring + endstring # return masked string.


# code wars description.

# Usually when you buy something, you're asked whether your credit card number, 
# phone number or answer to your most secret question is still correct. However, 
# since someone could look over your shoulder, you don't want that shown on your 
# screen. Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four 
# characters into '#'.