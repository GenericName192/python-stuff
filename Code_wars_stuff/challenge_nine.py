# function to find the unique char within an array
def find_uniq(arr):
    list_checker = []
    found_numbers = []
    for x in arr:
        if x in list_checker:
            list_checker.remove(x)
            found_numbers.append(x)
        else:
            if x in found_numbers: # otherwise its just readding the number its just removed.
                continue
            else:
                list_checker.append(x)
    if len(list_checker) > 0:
        return list_checker[0]

# code wars description

# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

# This is the first kata in series:

# Find the unique number (this kata)
# Find the unique string
# Find The Unique