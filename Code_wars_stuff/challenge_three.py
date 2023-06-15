# Takes a string then returns the middle or middle 2 values depending on if the
# length of the string is even or odd.
def get_middle(s):
    length = len(s)
    if length % 2 == 0: # The number is even
        cut_from = length // 2 - 1
        cut_to = length // 2 + 1
        return s[cut_from : cut_to]
    else: # The number is odd
        cut_from = length // 2
        cut_to = length // 2 + 1
        return s[cut_from : cut_to]

# code wars description.

# You are going to be given a word. Your job is to return the middle character 
# of the word. If the word's length is odd, return the middle character. If the
# word's length is even, return the middle 2 characters.