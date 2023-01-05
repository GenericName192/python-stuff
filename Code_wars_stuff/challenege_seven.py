# function to see if there are the same number of X's and O's
def xo(s):
    x_count = 0
    o_count = 0

    for x in s:
        if x.upper() == "X": # Upper used to make it case insensitive.
            x_count += 1
        elif x.upper() == "O":
            o_count += 1

    if x_count == o_count:
        return True

    else:
        return False

# code wars description

# Check to see if a string has the same amount of 'x's and 'o's. The method must
# return a boolean and be case insensitive. The string can contain any char.