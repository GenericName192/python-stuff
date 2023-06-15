# Wasnt sure how to format things correctly in one go so i made a function to do it
def formatting(number):
    number = str(number)
    if len(number) == 1:
        return "0" + number
    return number

# turns seconds into hour:min:seconds
def make_readable(seconds):
    hour = 0
    min = 0
    while seconds >= 3600:
        seconds -= 3600
        hour += 1
    while seconds >= 60:
        seconds -= 60
        min += 1

    return formatting(hour) + ":" + formatting(min) + ":" + formatting(seconds)

# code wars description

# Write a function, which takes a non-negative integer (seconds) as input and 
# returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)