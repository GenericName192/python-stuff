# Function that takes an iterable and removes any duplicates that are next to each other.
def unique_in_order(iterable):
    if len(iterable) == 0:
        return [] # incase the iterable is empty
    new_list = [iterable[0]] # The first char or the iterable will always be unique so added straight away.
    index = 0
    for x in iterable:
        if x == new_list[index]: # If the char is equal to the previous one.
            continue
        else: # If the char is unique its added and the index is increased.
            index += 1
            new_list.append(x)
    return new_list

# code wars description

# Implement the function unique_in_order which takes as argument a sequence and 
# returns a list of items without any elements with the same value next to each 
# other and preserving the original order of elements.