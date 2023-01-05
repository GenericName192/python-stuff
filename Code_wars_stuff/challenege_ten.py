# function to split a string into a list of 2 chars at a time, if an odd numbered string is given it adds a _
def solution(s):
    arr = []
    if len(s) % 2 == 1: # if the length is an odd number
        s += "_"
    while len(s) > 0:
        arr.append(s[:2])
        s = s[2:]
    return arr

# code wars description 

# Complete the solution so that it splits the string into pairs of two 
# characters. If the string contains an odd number of characters then it should 
# replace the missing second character of the final pair with an underscore ('_').